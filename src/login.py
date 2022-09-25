from telegram.client import Telegram
import os

tg = Telegram(
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    phone=os.getenv("PHONE"),
    database_encryption_key="changeme1234",
)

tg.login()