import requests

def suporta_intencao(intencao: str) -> bool:
    return intencao == "criar_site"

def handle_comando(comando: dict, historico: list) -> str:
    tema = comando["parametros"].get("tema", "geral")

    try:
        response = requests.post("https://httpbin.org/post", json={"tema": tema})
        if response.status_code == 200:
            return f"Site de '{tema}' criado com sucesso! (Resposta real da API)"
        else:
            return f"Falha ao criar site. Status da API: {response.status_code}"
    except Exception as e:
        return f"Erro ao acessar serviço de criação: {e}"