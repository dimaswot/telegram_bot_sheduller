from flask import Flask, request
import requests
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update

from datetime import timedelta

#https://api.telegram.org/bot1541592659:AAHAdbQr6NyQW0eXmhOFXR8A8CVP-2zEB0k/setWebhook?url=https://a50898718247.ngrok.io/

app = Flask(__name__)

CHAT_ID = 742632933

token = "1541592659:AAHAdbQr6NyQW0eXmhOFXR8A8CVP-2zEB0k"
url = "https://telegram1bot1ksrpo.herokuapp.com/"
updater = Updater(token, use_context=True)


@app.route(f"/{token}", methods=["GET", "POST"])
def receive_update():
    update: Update = telegram.Update.de_json(request.json, updater.bot)
    updater.dispatcher.process_update(update)
    print(update.message.text)
    print(update.message.chat_id)
    updater.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    return {"ok": True}


@app.route("/setWebhook")
def set_webhook():
    updater.bot.set_webhook(
        f'{url}/{token}'
    )
    return 'ok'

def din():
    updater.bot.send_message(chat_id=CHAT_ID,text="Мне тебе хочется повторить, что пора учить!")
    pass


def don():
    updater.bot.send_message(chat_id=CHAT_ID, text="Это сообщение пришло в определнное время")
    pass

def bom():
    updater.bot.send_message(chat_id=CHAT_ID, text="Это сообщение пришло в определнное время")
    pass
