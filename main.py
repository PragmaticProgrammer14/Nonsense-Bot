import telebot as tb
import random
import os
from dotenv import load_dotenv

text_reply = ["I'm not going to do anything.", "Stop bothering me!", "Pls stop!"]

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = tb.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def welcome_message(message):
    bot.reply_to(message, text="Hello, I'm completely useless bot. I'm doing nothing, no matter what you are going to type.")

@bot.message_handler(commands=["help"])
def welcome_message(message):
    bot.reply_to(message, text="I'm useless bot. This is the only thing, you should to know")

@bot.message_handler(content_types=["text"])
def send_message(message):
    reply = random.choice(text_reply)
    bot.reply_to(message, reply)

@bot.message_handler(content_types=["photo"])
def reply_to_photo(message):
    bot.reply_to(message, "Cool photo (maybe), but leave me alone, I'm tired.")

@bot.message_handler(content_types=["sticker"])
def send(message):
    bot.reply_to(message, "Cool sticker, but I don't care")

bot.infinity_polling()