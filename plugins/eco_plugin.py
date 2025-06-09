def suporta_intencao(intencao: str) -> bool:
    return intencao == "eco"

def handle_comando(comando: dict, historico: list) -> str:
    ultima_msg = historico[-1][0] if historico else ""
    return f"ECO: {ultima_msg}"