from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Update
from github import GitHubManager
from detector import detect_errors
from claude import ClaudeClient
from loop import CorrectionLoop

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.app = ApplicationBuilder().token(token).build()

    async def start(self, update: Update, context):
        await update.message.reply_text("🤖 Orquestrador ativo!\nEnvie o link do repositório GitHub.")

    async def handle_repo(self, update: Update, context):
        repo_url = update.message.text.strip()
        if "github.com" not in repo_url:
            await update.message.reply_text("❌ Link inválido. Envie um repositório do GitHub.")
            return

        await update.message.reply_text(f"🔗 Recebido: {repo_url}\n🔄 Iniciando análise...")

        env = load_env_vars()
        gh = GitHubManager(env["GITHUB_TOKEN"])
        claude = ClaudeClient(env["CLAUDE_API_KEY"])
        path = "./repositorio_trabalho"

        try:
            gh.clone(repo_url, path)
            errors = detect_errors(path)
            if not errors:
                await update.message.reply_text("✅ Nenhum erro encontrado!")
                return

            correction_loop = CorrectionLoop(gh, claude, path, repo_url)
            result = correction_loop.run()
            await update.message.reply_text(result or "✅ Correções aplicadas.")
        except Exception as e:
            await update.message.reply_text(f"❌ Erro: {str(e)}")

    def run(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_repo))
        self.app.run_polling()
