from django.shortcuts import get_object_or_404, render, redirect
import telebot
from .models import Project

TELEGRAM_BOT_TOKEN = '7076657023:AAGDE4d71JX2MN8_WBwgN0VgUGk2p7Bh-6w'
TELEGRAM_CHAT_ID = '-4142096315'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def _is_spam(request):
    """Honeypot-проверка вместо reCAPTCHA.

    В формах есть скрытое поле name="website", невидимое для человека.
    Боты, заполняющие все поля подряд, в него что-то впишут — такую
    заявку молча отбрасываем. Реальные пользователи поле не видят и
    оставляют пустым.
    """
    return bool((request.POST.get('website') or '').strip())


def _send_order(request):
    """Собирает заявку из POST и шлёт в Telegram."""
    name = request.POST.get('name')
    email = request.POST.get('email')
    telephone = request.POST.get('telephone')
    textarea = request.POST.get('Textarea')
    message = (
        f"Новый заказ!\n"
        f"Имя: {name}\n"
        f"Email: {email}\n"
        f"Телефон: {telephone}\n"
        f"Описание: {textarea}"
    )
    bot.send_message(TELEGRAM_CHAT_ID, message)


def index(request):
    if request.method == "POST":
        if not _is_spam(request):
            _send_order(request)
        # Ботам тоже отдаём «спасибо», чтобы не палить honeypot.
        return redirect('thanks')
    return render(request, 'index.html')


def portfolio(request):
    if request.method == "POST":
        if not _is_spam(request):
            _send_order(request)
        return redirect('thanks')
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})


def portfolio_ident(request, id):
    if request.method == "POST":
        if not _is_spam(request):
            _send_order(request)
        return redirect('thanks')
    project = get_object_or_404(Project, id=id)
    return render(request, 'portfolio.html', {'project': project})


def contact(request):
    if request.method == "POST":
        if not _is_spam(request):
            _send_order(request)
        return redirect('thanks')
    return render(request, 'contact.html')


def prices(request):
    if request.method == "POST":
        if not _is_spam(request):
            _send_order(request)
        return redirect('thanks')
    return render(request, 'prices.html')


def service_detail(request, service_name):
    if request.method == "POST":
        if not _is_spam(request):
            _send_order(request)
        return redirect('thanks')
    return render(request, 'service-detail.html', {'service_name': service_name})


def thanks(request):
    return render(request, 'thanks.html')


def robots_txt(request):
    from django.http import HttpResponse
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Sitemap: https://nes-agency.ru/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
