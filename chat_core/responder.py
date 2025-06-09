# chat_core/responder.py
from chat_core.plugin_loader import carregar_plugins

plugins = carregar_plugins()

def responder(mensagem, historico):
    for plugin in plugins:
        try:
            resposta = plugin.handle(mensagem, historico)
            if resposta:
                return resposta
        except Exception as e:
            print(f"Erro no plugin {plugin.__name__}: {e}")
    return "Desculpe, não entendi. (nenhum plugin respondeu)"