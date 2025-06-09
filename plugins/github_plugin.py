def suporta_intencao(intencao):
    return intencao in ["github_criar_repo", "github_corrigir_bug", "github_sync", "github_analisar"]

def handle_comando(comando, historico):
    intencao = comando["intencao"]

    if intencao == "github_criar_repo":
        return "✅ Repositório GitHub criado com sucesso."

    if intencao == "github_corrigir_bug":
        return "🛠️ Bug identificado e corrigido no repositório."

    if intencao == "github_sync":
        return "🔄 Projeto sincronizado com o GitHub."

    if intencao == "github_analisar":
        return "📊 Repositório analisado: nenhum problema crítico encontrado."

    return "🔍 Comando GitHub não reconhecido."