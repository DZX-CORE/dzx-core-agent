import os
from dotenv import load_dotenv

def load_env_vars():
    load_dotenv()
    return {
        "TELEGRAM_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN"),
        "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
        "CLAUDE_API_KEY": os.getenv("CLAUDE_API_KEY")
    }
