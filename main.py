from bot import TelegramBot
from config import load_env_vars

def main():
    env = load_env_vars()
    bot = TelegramBot(env["TELEGRAM_TOKEN"])
    bot.run()

if __name__ == "__main__":
    main()