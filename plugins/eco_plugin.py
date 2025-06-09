# plugins/eco_plugin.py
def handle(mensagem, historico):
    if "eco" in mensagem.lower():
        return "ECO: " + mensagem
    return None