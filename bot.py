import os
import logging
import requestshttps://github.com/KocekElena/prace_bot/tree/main
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Základní nastavení
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Jednoduché "vyhledávání" (zatím jen testovací zpráva)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ahoj! Tohle je pracovní bot. Napiš /hledat a ukážu ti nové nabídky.")

async def hledat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Zde bude skutečné vyhledávání — zatím testovací data
    jobs = [
        "🔹 Obchodní zástupce – Děčín\nhttps://www.jobs.cz/rnd123",
        "🔹 Datový analytik junior – Liberec\nhttps://www.jobs.cz/rnd456",
        "🔹 Technik vzduchotechniky – Rumburk\nhttps://www.jobs.cz/rnd789"
    ]
    await update.message.reply_text("Dnešní nabídky:\n\n" + "\n\n".join(jobs))

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hledat", hledat))

    app.run_polling()
