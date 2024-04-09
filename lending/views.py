from django.shortcuts import render
import telebot

TELEGRAM_BOT_TOKEN ='7128625164:AAG2ZwTPyN8-xkNoIP0wmRNjG-pzIBI1Ncw'
TELEGRAM_CHAT_ID = '543664962'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def home(request):
    #bot.send_message(TELEGRAM_CHAT_ID, 'Site is online')
    return render(request, 'home.html')

def tsg(request):
    return render(request, 'tsg.html')

def portfolio(request):
    return render(request, 'portfolio.html')