import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = 'YOUR_TOKEN_HERE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Nr1Calls Bot Online! /vip for VIP access.")

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = f"""
🔥 NR1 VIP ACCESS 🔥

Send 2 SOL to:
`6nE3bfze56BwNemx78TdrkJAD9x4pGhiMuhC1ruPgfti`

After sending type /done
    """
    await update.message.reply_text(msg, parse_mode='Markdown')

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Confirmed! VIP link incoming. Nr1 team.")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("vip", vip))
    application.add_handler(CommandHandler("done", done))
    application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
