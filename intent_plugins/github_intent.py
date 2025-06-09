class GitHubIntent:
    @staticmethod
    def detectar(mensagem: str):
        mensagem = mensagem.lower()

        if "criar repositório" in mensagem or "novo repo" in mensagem:
            return {"intencao": "github_criar_repo"}

        if "corrigir bug" in mensagem or "arrumar erro" in mensagem:
            return {"intencao": "github_corrigir_bug"}

        if "sincronizar projeto" in mensagem or "atualizar no github" in mensagem:
            return {"intencao": "github_sync"}

        if "analisar repositório" in mensagem or "verificar repo" in mensagem:
            return {"intencao": "github_analisar"}

        return None