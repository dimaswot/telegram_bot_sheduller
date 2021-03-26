from flask import Flask, request
import requests
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, CallbackContext, Filters, CallbackQueryHandler
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import timedelta

#https://api.telegram.org/bot1693338559:AAFniq64i8lKTKVWjGdq9_9lDki1W4SK3X8/setWebhook?url=https://62ec6641b1df.ngrok.io

app = Flask(__name__)
sched = BlockingScheduler()
CHAT_ID = 742632933

token = "1693338559:AAFniq64i8lKTKVWjGdq9_9lDki1W4SK3X8"
url = "https://telegram1bot1ksrpo.herokuapp.com"
updater = Updater(token, use_context=True)


@app.route(f"/{token}", methods=["GET", "POST"])
def receive_update():
    print(update.message.text)
    sched.start();
    print(update.message.chat_id)
    update: Update = telegram.Update.de_json(request.json, updater.bot)
    updater.dispatcher.process_update(update)
    
    update.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
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


@sched.scheduled_job('interval', minutes=1)
def print_interval():
    din()

@sched.scheduled_job('cron', day_of_week='fri', hour='15-19/2', timezone='Europe/Moscow')
def print_one():
    don()


@sched.scheduled_job('cron', day_of_week='fri', hour='12', minute='48', timezone='Europe/Moscow')
def print_one_crone():
    updater.bot.send_message(chat_id=CHAT_ID, text="Это сообщение пришло в определнное время 12 48")

