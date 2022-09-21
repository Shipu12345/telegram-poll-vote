from telegram.client import Telegram
import os

tg = Telegram(
    api_id="14353957",
    api_hash="546d35bf484f7e85c71d566a6d95f239",
    phone="+8801991628369",
    database_encryption_key="changeme1234",
)

tg.login()