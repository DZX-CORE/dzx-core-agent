class GitHubPlugin:
    def suporta_intencao(self, intencao: str) -> bool:
        return intencao in [
            "github_analisar",
            "github_criar",
            "github_listar"
        ]

    def handle_comando(self, comando: dict, historico: list) -> str:
        intencao = comando["intencao"]

        if intencao == "github_analisar":
            return "🔍 Analisando o repositório... (simulado)"

        elif intencao == "github_criar":
            return "📁 Criando um novo repositório no GitHub... (simulado)"

        elif intencao == "github_listar":
            return "📃 Listando seus repositórios... (simulado)"

        return "❌ Comando não reconhecido pelo plugin do GitHub."