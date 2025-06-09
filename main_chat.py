import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Garante execução a partir da raiz do projeto

from chat_core.intent_detector import detectar_intencao
from chat_core.plugin_loader import carregar_plugins
import gradio as gr

plugins = carregar_plugins()

def responder(mensagem, historico):
    comando = detectar_intencao(mensagem)
    if not comando:
        return "Desculpe, não entendi. (intenção não identificada)"

    for plugin in plugins:
        try:
            if plugin.suporta_intencao(comando["intencao"]):
                resposta = plugin.handle_comando(comando, historico)
                if resposta:
                    return resposta
        except Exception as e:
            print(f"Erro no plugin {plugin.__class__.__name__}: {e}")

    return "Nenhum plugin disponível para essa tarefa."

iface = gr.ChatInterface(
    fn=responder,
    title="dzx-core-Agent",
    description="Chat modular com plugins de intenção",
    theme="default"
)

iface.launch()