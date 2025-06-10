class CorrectionLoop:
    def __init__(self, gh, claude, path, repo_url):
        self.gh = gh
        self.claude = claude
        self.path = path
        self.repo_url = repo_url

    def run(self):
        attempts = 0
        while attempts < 3:
            errors = detect_errors(self.path)
            if not errors:
                return "✅ Nenhum erro detectado!"

            suggestion = self.claude.analyze("\n".join(errors), "")
            print("💡 Sugestão:", suggestion)

            # Aqui ficaria a lógica real de aplicar a correção
            print("🛠️ Aplicando correção...")
            attempts += 1

        return "⚠️ Máximo de tentativas atingido."
