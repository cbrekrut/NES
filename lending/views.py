from django.shortcuts import get_object_or_404, render
import telebot
from .models import Project
from django.shortcuts import redirect
from django.contrib import messages
TELEGRAM_BOT_TOKEN ='7128625164:AAG2ZwTPyN8-xkNoIP0wmRNjG-pzIBI1Ncw'
TELEGRAM_CHAT_ID = '543664962'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
import requests
def verify_recaptcha(response_token):
    secret_key = '6LdDOcspAAAAAJPVW3GEKGSgPzU85HiiCEbPFXtz'
    data = {
        'secret': secret_key,
        'response': response_token
    }
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    response = requests.post(verify_url, data=data)
    return response.json()
def home(request):

    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        result = verify_recaptcha(recaptcha_response)
        if result.get('success'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            telephone = request.POST.get('telephone')
            textarea = request.POST.get('Textarea')
            message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
            bot.send_message(TELEGRAM_CHAT_ID, message)
            return redirect('/thanks')
        else:
            messages.error(request, 'Ошибка проверки reCAPTCHA. Пожалуйста, попробуйте еще раз.')
    return render(request, 'index.html')

def tsg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'tsg.html')
def md(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'metall-design.html')
def nanopi(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'nanopi.html')

def portfolio(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    projects = Project.objects.all()
    return render(request, 'portfolio.html',{'projects':projects})

def portfolio_ident(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    project = get_object_or_404(Project, id=id)
    return render(request, 'portfolio.html',{'project':project})

def priliv(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'priliv.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name == '':
            name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'contact.html')

def prices(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'prices.html')

def thanks(request):
    return render(request, 'thanks.html')