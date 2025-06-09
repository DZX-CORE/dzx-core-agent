def detectar_intencao(mensagem: str) -> dict | None:
    if "eco" in mensagem.lower():
        return {"intencao": "eco", "parametros": {}}
    return None