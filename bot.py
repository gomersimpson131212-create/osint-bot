from telegram.ext import Updater, CommandHandler
import requests
from db import init_db

conn, cursor = init_db()

def github(update, context):
    if not context.args:
        update.message.reply_text("Укажи username!")
        return
    username = context.args[0]
    r = requests.get(f"https://api.github.com/users/{username}")
    if r.status_code == 200:
        data = r.json()
        cursor.execute("INSERT INTO profiles (source, username, data) VALUES (?, ?, ?)",
                       ("GitHub", username, str(data)))
        conn.commit()
        update.message.reply_text(f"Сохранил данные о {username}")
    else:
        update.message.reply_text("Ошибка запроса")

def help_command(update, context):
    help_text = """
📜 Меню команд:
- /github username — сохранить GitHub профиль
- /news — собрать новости
- /search keyword — поиск по базе
- /alert keyword — добавить alert
- /listalerts — список alert'ов
- /removealert keyword — удалить alert
- /whois domain.com — WHOIS домена
- /ipinfo IP — инфа по IP
- /stats — статистика базы
- /randomfact — случайный факт
- /gaz — мемная команда
- /meme — мемный ответ
- /help — показать меню команд
"""
    update.message.reply_text(help_text)

updater = Updater("8871623776:AAFUiK_rZizgVhIyhZHRBIx-3WTCcRySqyg")  # вставь сюда токен от BotFather
updater.dispatcher.add_handler(CommandHandler("github", github))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.start_polling()
