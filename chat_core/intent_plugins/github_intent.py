def detectar(mensagem):
    if "atualize o repositório" in mensagem.lower():
        return {
            "intencao": "atualizar_repositorio",
            "parametros": {}
        }
    return None