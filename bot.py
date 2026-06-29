import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = 'YOUR_TOKEN_HERE'

def start(update, context):
    update.message.reply_text("🚀 Nr1Calls Bot is live! /vip for VIP.")

def vip(update, context):
    msg = """
🔥 NR1 VIP ACCESS 🔥

Send 2 SOL to:
`6nE3bfze56BwNemx78TdrkJAD9x4pGhiMuhC1ruPgfti`

After sending type /done
    """
    update.message.reply_text(msg)

def done(update, context):
    update.message.reply_text("✅ Confirmed! VIP access granted soon.")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('vip', vip))
updater.dispatcher.add_handler(CommandHandler('done', done))

updater.start_polling()
updater.idle()
