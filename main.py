
import os
import asyncio
from orquestrador.github_manager import GitHubManager
from orquestrador.claude_client import ClaudeClient
from orquestrador.error_detector import ErrorDetector
from orquestrador.correction_loop import CorrectionLoop
from orquestrador.telegram_bot import TelegramBot

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

PASTA_PROJETO = "./repositorio_trabalho"
BRANCH_CORRECAO = "correcao-automatica"

github_manager = GitHubManager(GITHUB_TOKEN)
claude_client = ClaudeClient(CLAUDE_API_KEY)

async def callback_repositorio(repo_url, update, context):
    pasta = PASTA_PROJETO
    github_manager.clonar_repositorio(repo_url, pasta)

    error_detector = ErrorDetector(pasta)
    correction_loop = CorrectionLoop(
        github_manager, claude_client, error_detector,
        pasta, repo_url.split("github.com/")[-1].replace(".git", ""), BRANCH_CORRECAO
    )

    correction_loop.executar_loop_correcao()
    await update.message.reply_text("Loop de correção finalizado ou interrompido.")

def main():
    bot = TelegramBot(TELEGRAM_TOKEN, callback_repositorio)
    bot.iniciar_bot()

if __name__ == "__main__":
    main()