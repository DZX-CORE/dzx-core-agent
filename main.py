import gradio as gr

def responder(mensagem, historico):
    if historico is None:
        historico = []
    resposta = f"Você disse: {mensagem}"
    historico.append((mensagem, resposta))
    return historico

chat = gr.ChatInterface(
    fn=responder,
    title="Chat Simples Estilo ChatGPT",
    description="Converse com este chat simples.",
    examples=["Olá", "Como você está?", "Qual seu nome?"],
)

if __name__ == "__main__":
    chat.launch(server_name="0.0.0.0", server_port=8080)