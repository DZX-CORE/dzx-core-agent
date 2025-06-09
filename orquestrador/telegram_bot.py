import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

class TelegramBot:
    def __init__(self, token, callback_ao_receber_repositorio):
        self.token = token
        self.callback = callback_ao_receber_repositorio
        self.app = ApplicationBuilder().token(token).build()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Orquestrador ativo! Envie o link do seu repositório GitHub para iniciar a análise.")

    async def receber_repositorio(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        texto = update.message.text
        if "github.com" in texto:
            await update.message.reply_text(f"Repositório recebido: {texto}\nIniciando análise e correção.")
            await self.callback(texto, update, context)
        else:
            await update.message.reply_text("Por favor, envie um link válido de repositório GitHub.")

    def iniciar_bot(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.receber_repositorio))
        self.app.run_polling()
