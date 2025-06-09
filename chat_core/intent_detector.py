import re

def detectar_intencao(mensagem: str) -> dict | None:
    msg = mensagem.lower()

    # Exemplo básico: detecta pedido para criar site
    match = re.search(r"crie um site(?: de)? (.+)", msg)
    if match:
        tema = match.group(1).strip()
        return {
            "intencao": "criar_site",
            "parametros": {"tema": tema}
        }

    # Exemplo: eco
    if "eco" in msg:
        return {
            "intencao": "eco",
            "parametros": {}
        }

    # Nenhuma intenção detectada
    return None