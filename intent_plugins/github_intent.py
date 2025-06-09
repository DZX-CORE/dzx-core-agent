class GitHubIntent:
    def detectar(self, mensagem: str):
        mensagem = mensagem.lower()

        if "analisar" in mensagem and "repositório" in mensagem:
            return {"intencao": "github_analisar"}

        if "criar" in mensagem and "repositório" in mensagem:
            return {"intencao": "github_criar"}

        if "listar" in mensagem and "repositório" in mensagem:
            return {"intencao": "github_listar"}

        return None