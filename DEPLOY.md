# Деплой NES@Agency

Боевой сайт **nes-agency.ru** хостится на **Beget** (IP 31.31.198.49) и работает
как Django-приложение под **Phusion Passenger** (Python 3.10), статику отдаёт
nginx Beget'а. Это не Docker — обновление идёт через `git pull` на сервере и
перезапуск Passenger.

> Приложение уже развёрнуто. Ниже — шаги **обновления** на новую версию,
> а не первичной установки (виртуальное окружение и `passenger_wsgi.py`
> настроены в панели Beget).

## 0. Один раз: секретный ключ

`SECRET_KEY` берётся из переменной окружения `DJANGO_SECRET_KEY`. В панели Beget
(раздел Python-приложения → переменные окружения) задайте:

```
DJANGO_SECRET_KEY = <длинный случайный ключ>
```

Сгенерировать ключ:

```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

Если переменную не задать — приложение поднимется на небезопасном фолбэке из
`settings.py` (для публичного репозитория так оставлять не стоит).

`DJANGO_DEBUG` на проде **не задаём** → `DEBUG = False`.

## 1. Залить новую версию

Прод тянет ветку `main`. Сначала влить редизайн в `main` (локально или в GitHub):

```bash
git checkout main && git merge --no-ff design-refresh && git push origin main
```

## 2. На сервере Beget (SSH или терминал в панели)

```bash
cd ~/nes-agency.ru            # каталог приложения (уточнить в панели)
git pull origin main

# зависимости (в venv приложения)
pip install -r requirements.txt

# миграции (если менялись модели — сейчас нет, но шаг безопасен)
python manage.py migrate --noinput

# собрать статику туда, откуда nginx отдаёт /static/  (папка static/)
python manage.py collectstatic --noinput

# перезапустить Passenger
mkdir -p tmp && touch tmp/restart.txt
```

## 3. Проверка

```bash
curl -sI https://nes-agency.ru | head -1          # 200
curl -s -o /dev/null -w "%{http_code}\n" \
  https://nes-agency.ru/static/css/nes-refresh.css # 200 — стили на месте
```

Открыть сайт, проверить: главная, /prices/, /contact/ (отправка формы →
страница «Спасибо», заявка приходит в Telegram), /portfolio/, sitemap.xml,
robots.txt.

## Заметки

- **Статика.** `STATIC_ROOT = BASE_DIR/'static'` совпадает с папкой, откуда
  nginx Beget'а уже отдаёт `/static/`. После каждого деплоя обязательно
  `collectstatic`, иначе обновлённый CSS не подхватится.
- **Формы.** Заявки уходят в Telegram (`lending/views.py`), e-mail-бэкенд не
  используется. Антиспам — honeypot-поле `website` (reCAPTCHA убрана).
- **ALLOWED_HOSTS** — только `nes-agency.ru` и `www.nes-agency.ru`
  (`localhost` добавляется автоматически лишь при `DEBUG=True`).
- **База** — SQLite на сервере; `git pull` её не трогает (в репозитории лежит
  старый снимок, боевые данные живут на сервере).
