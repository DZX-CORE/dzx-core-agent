import re

def detectar_intencao(mensagem: str) -> dict | None:
    msg = mensagem.lower()
    if "github" in msg and "repositório" in msg:
        m = re.search(r"usuario (\w+)", msg)
        usuario = m.group(1) if m else None
        return {
            "intencao": "github_operacao",
            "parametros": {
                "acao": "listar_repos",
                "usuario": usuario
            }
        }
    return None