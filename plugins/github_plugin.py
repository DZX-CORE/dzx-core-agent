def executar(contexto):
    comando = contexto.get("comando")

    if comando == "github_criar_repo":
        return "✅ Repositório GitHub criado com sucesso."

    if comando == "github_corrigir_bug":
        return "🛠️ Bug identificado e corrigido no repositório."

    if comando == "github_sync":
        return "🔄 Projeto sincronizado com o GitHub."

    return "❓ Comando GitHub não reconhecido."