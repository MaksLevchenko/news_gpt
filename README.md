# Привет! Меня зовут Макс.
## Хочу представить свой проект по обработке новостей с сайта РБК, с использованием gigachat.

## Для начала нужно клонировать этот репозиторий на свой компьютер, для этого нужно в терминале набрать команду git clone https://github.com/MaksLevchenko/news_gpt

# Теперь займёмся запуском проекта:

## 1. Перейдите в корневой каталог проекта news_gpt

## 2. Установим и активируем виртуальное окружение Python, командами: python3 -m venv .venv , И активируем его командой: Для Windows: .venv\Scripts\activate. Для macOS и Linux: source .venv/bin/activate

## 3. Теперь нужно установить все зависимости проекта, делается это командой pip install -r requirements.txt

## 4. В каталоге news_gpt создайте файл .env и запишите в нём следующие переменные: BOT_TOKEN=<Ваш токен полученный у @BotFather в телеграм> И GIGACHAT_KEY=<Ваш Authorization key полученный вот здесь: https://developers.sber.ru/docs/ru/gigachat/quickstart/ind-using-api#poluchenie-avtorizatsionnyh-dannyh >

## 5. Осталось самое главное. Запустить нашего бота! Делается это запуском файла bot.py 

# Всё готово!!
