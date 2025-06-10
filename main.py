import sys
import os
from dotenv import load_dotenv

# Garante que a pasta atual esteja no sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orquestrador.utils import clonar_repositorio
from orquestrador.error_detector import detectar_erros
from orquestrador.claude_interface import gerar_resposta_claude
from orquestrador.github_interface import aplicar_corrigido
from orquestrador.telegram_bot import TelegramBot

# Carrega as variáveis de ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CLAUDE_TOKEN = os.getenv("CLAUDE_API_KEY")

# Função chamada ao receber link via Telegram
def callback_repositorio(link):
    path = "./repositorio_trabalho"

    if os.path.exists(path):
        print(f"Pasta {path} já existe, removendo...")
        os.system(f"rm -rf {path}")

    print(f"Clonando {link} para {path}...")
    clonar_repositorio(link, path)

    erros = detectar_erros(path)
    if not erros:
        print("✅ Nenhum erro detectado. Projeto parece estar OK.")
        return

    print("⚠️ Enviando erros para o Claude...")
    resposta = gerar_resposta_claude(erros, CLAUDE_TOKEN)

    print("🛠️ Aplicando correções propostas...")
    aplicar_corrigido(resposta, path, GITHUB_TOKEN, link)
    print("✅ Loop de correção finalizado ou interrompido.")

# Inicializa o bot
def main():
    print(f"Token TELEGRAM_TOKEN do .env: {TELEGRAM_TOKEN}")
    bot = TelegramBot(TELEGRAM_TOKEN, callback_repositorio)
    bot.run()

if __name__ == "__main__":
    main()