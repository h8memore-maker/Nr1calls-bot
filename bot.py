import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 'YOUR_BOT_TOKEN_HERE'   # We'll change this later

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Nr1Calls Insider Bot is live! Use /vip for VIP access.")

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """
🔥 NR1 VIP ACCESS 🔥

Send 2 SOL to:
`6nE3bfze56BwNemx78TdrkJAD9x4pGhiMuhC1ruPgfti`

After sending, type /done

This grants you access to the private/VIP group.
    """
    await update.message.reply_text(msg, parse_mode='Markdown')

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Confirmed! Private VIP group link coming soon. Nr1 team.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("done", done))
    app.run_polling()

if __name__ == '__main__':
    main()
