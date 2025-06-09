# 🧠 dzx-core-Agent

Um assistente de chat modular, leve e estável. Ideal para evoluir com ferramentas e plugins, sem quebrar o núcleo.

> ✅ Projeto criado para rodar no Google Colab usando GitHub como base de código.

---

## 🚀 Recursos

* ✅ Chat com interface visual (Gradio)
* 🔌 Suporte a plugins simples e seguros
* ↺ Núcleo imutável: adicione funcionalidades sem quebrar o sistema
* 💡 Fácil de manter e expandir

---

## 📁 Estrutura do projeto

```
dzx-core-Agent/
├── main_chat.py               # Inicia o Gradio (interface)
├── chat_core/
│   ├── responder.py           # Controla respostas usando plugins
│   └── plugin_loader.py       # Carrega plugins com segurança
├── plugins/
│   └── eco_plugin.py          # Exemplo de plugin funcional
├── requirements.txt           # Dependências
└── README.md                  # Este arquivo
```

---

## ▶️ Como rodar no Google Colab

> ✅ Requer: conta no GitHub + Colab

1. Copie o link do seu repositório no GitHub (ex: `https://github.com/seu-usuario/dzx-core-Agent`)
2. Abra o Google Colab
3. Rode as células abaixo:

```python
# Clone o projeto
!git clone https://github.com/seu-usuario/dzx-core-Agent.git
%cd dzx-core-Agent

# Instale as dependências
!pip install -r requirements.txt

# Inicie o chat (link público será exibido)
!python3 main_chat.py
```

---

## 🔌 Criar um novo plugin

Crie um novo arquivo `.py` dentro da pasta `plugins/`.
Exemplo: `plugins/saudacao.py`

```python
# plugins/saudacao.py
def handle(mensagem, historico):
    if "olá" in mensagem.lower():
        return "Olá! Como posso ajudar você hoje?"
    return None
```

> O plugin **deve ter uma função chamada \*\*\*\*`handle(mensagem, historico)`**.
> Se retornar algo diferente de `None`, o chat mostra a resposta.

---

## 🛡️ Segurança e estabilidade

* O núcleo (`main_chat.py`, `responder.py`, `plugin_loader.py`) **nunca deve ser alterado diretamente.**
* Plugins com erro são ignorados automaticamente, sem travar o chat.
* Toda melhoria deve ser feita em forma de **novo plugin.**

---

## 🧠 Objetivo futuro

Este projeto foi pensado para crescer com:

* Acesso a APIs
* Execução de comandos
* Manipulação de arquivos
* Ferramentas personalizadas
* Tudo via **plugins isolados**

---

## 👤 Autor

Desenvolvido com auxílio da IA (ChatGPT) e mantido por [DZX-CORE].

---
