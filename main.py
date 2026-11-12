# telebot  =>  pip install pytelegrambotapi

import telebot 

from telebot import *
 
bot = telebot.TeleBot("8809466266:AAGRfkX8dpRDiu88fqH1zAHmOddJehNcmXA")

# @bot.message_handler(commands=["boshlash", "start"])
# def xabarUlash(message):
#     bot.reply_to(message, text="botimizga xush kelibsiz!!!")


@bot.message_handler(["read"])
def bajar(message):
    bot.reply_to(message, text= "Salom bu mening 1chi telebotdagi kodim!!!")

print("working...")
bot.infinity_polling()