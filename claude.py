class ClaudeClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze(self, logs, code):
        print("🧠 Enviando logs para análise...")
        return f"Sugestão: {logs[:300]}"
