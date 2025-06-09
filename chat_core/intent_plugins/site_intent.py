import re

def detectar(mensagem):
    msg = mensagem.lower()
    match = re.search(r"crie um site(?: de)? (.+)", msg)
    if match:
        tema = match.group(1).strip()
        return {
            "intencao": "criar_site",
            "parametros": {"tema": tema}
        }
    return None