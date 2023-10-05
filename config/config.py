import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_APIKEY = os.environ.get("OPENAI_APIKEY")

    TELEGRAM_BOT = os.environ.get("TELEGRAM_BOT")