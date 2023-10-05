from config.config import Config
from telegram.ext import ApplicationBuilder
from bot.bot import hello_command, reply_command

config = Config()

TELEGRAMBOT_TOKEN = config.TELEGRAM_BOT

app = ApplicationBuilder().token(TELEGRAMBOT_TOKEN).build()

app.add_handler(hello_command)
app.add_handler(reply_command)