import gradio as gr

def responder(mensagem, historico):
    resposta = f"Você disse: {mensagem}"
    historico.append((mensagem, resposta))
    return historico

chat = gr.ChatInterface(
    fn=responder,
    title="Chat Simples Estilo ChatGPT",
    description="Converse com este chat simples, estilo ChatGPT, usando apenas Gradio.",
    theme="soft",  # visual mais limpo
    examples=["Olá!", "Como você está?", "O que você pode fazer?"],
    retry_btn="Tentar novamente",
    undo_btn="Desfazer",
    clear_btn="Limpar",
)

if __name__ == "__main__":
    chat.launch(server_name="0.0.0.0", server_port=8080)