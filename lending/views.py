from django.shortcuts import render
from telegram import Bot
def send_notification(text):
    bot = Bot(token='7128625164:AAG2ZwTPyN8-xkNoIP0wmRNjG-pzIBI1Ncw')
    chat_id = "543664962"
    bot.send_message(chat_id=chat_id, text=text)

def home(request):
    user = request.user
    send_notification(user,'visit your home page')
    return render(request, 'home.html')

def tsg(request):
    return render(request, 'tsg.html')

def portfolio(request):
    return render(request, 'portfolio.html')