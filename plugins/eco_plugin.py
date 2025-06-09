# plugins/eco_plugin.py
def handle(mensagem, historico):
    if "eco" in mensagem.lower():
        return "Você chamou por eco? Estou aqui!"
    return None
