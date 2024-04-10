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
def md(request):
    return render(request, 'metall-design.html')
def nanopi(request):
    return render(request, 'nanopi.html')
def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        
        bot.send_message(TELEGRAM_CHAT_ID, message)

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')