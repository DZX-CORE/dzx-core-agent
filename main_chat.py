# main_chat.py
import gradio as gr
from chat_core.responder import responder

chat = gr.ChatInterface(
    fn=responder,
    title="Assistente Modular",
    description="Chat modular pronto para evoluir.",
)

if __name__ == "__main__":
    chat.launch(server_name="0.0.0.0", server_port=8080)