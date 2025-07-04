import os
import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
import sqlite3
import requests
import asyncio

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_ID = 123456789  # Substitua pelo seu ID

# Configuração do logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Banco de dados
def init_db():
    conn = sqlite3.connect("jogos.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jogos (id INTEGER PRIMARY KEY AUTOINCREMENT, dezenas TEXT)''')
    conn.commit()
    conn.close()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [['📝 Meus Jogos', '🎯 Conferir Resultado'], ['➕ Adicionar Jogo', '❌ Remover Jogo']]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    await update.message.reply_text("📲 Escolha uma opção:", reply_markup=reply_markup)

# Coloque aqui os outros handlers e lógica do bot (omitido para brevidade)

def main():
    init_db()
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # Adicione os outros handlers aqui
    application.run_polling()

if __name__ == "__main__":
    main()