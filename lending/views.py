from django.shortcuts import get_object_or_404, render
import telebot
from .models import Project
from django.shortcuts import redirect
from django.contrib import messages
TELEGRAM_BOT_TOKEN ='7076657023:AAGDE4d71JX2MN8_WBwgN0VgUGk2p7Bh-6w'
TELEGRAM_CHAT_ID = '-4142096315'
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
from django.http import JsonResponse

def index(request):
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
            return redirect('thanks')
        else:
            return render(request, 'index.html',{'alert':True})
    return render(request, 'index.html')

def portfolio(request):
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
            return redirect('thanks')
        else:
            projects = Project.objects.all()
            return render(request, 'portfolio.html',{'alert':True})
    projects = Project.objects.all()
    return render(request, 'portfolio.html',{'projects':projects})

def portfolio_ident(request, id):
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
            return redirect('thanks')
        else:
            project = get_object_or_404(Project, id=id)
            return render(request, 'portfolio.html',{'alert':True, 'project':project})
    project = get_object_or_404(Project, id=id)
    return render(request, 'portfolio.html',{'project':project})



def contact(request):
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
            return redirect('thanks')
        else:
            return render(request, 'contact.html',{'alert':True})
    return render(request, 'contact.html')

def prices(request):
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
            return redirect('thanks')
        else:
            return render(request, 'prices.html',{'alert':True})
    return render(request, 'prices.html')
    
def service_detail(request, service_name):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        textarea = request.POST.get('Textarea')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nОписание: {textarea}"
        bot.send_message(TELEGRAM_CHAT_ID, message)
        return redirect('/thanks')
    return render(request, 'service-detail.html', {'service_name': service_name})

def thanks(request):
    return render(request, 'thanks.html')