from telegram.client import Telegram
import os

tg = Telegram(
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    phone=os.getenv("PHONE"),
    database_encryption_key="changeme1234",
)


def get_all_chats():
    result = tg.get_chats()
    result.wait()

    # if result.error:
    #     print(f"get chats error: {result.error_info}")
    # else:
    #     print(f"chats: {result.update}")


def get_history():
    result = tg.get_chat_history(chat_id=-1001557909306)
    result.wait()

    if result.error:
        print(f"get history error: {result.error_info}")
    else:
        print(f"history: {result.update}")


def get_message():
    result = tg.get_message(chat_id=-1001557909306, message_id=59768832)
    result.wait()

    # if result.error:
    #     print(f"get message error: {result.error_info}")
    # else:
    #     print(f"message: {result.update}")


def vote():
    params = {
        "chat_id": -1001557909306,
        "message_id": 59768832,
        "option_ids": [0],
    }
    result = tg.call_method("setPollAnswer", params)
    result.wait()

    if result.error:
        print(f"send message error: {result.error_info}")
    else:
        print(f"message has been sent: {result.update}")


def main():
    tg.login()
    get_all_chats()
    get_history()
    # get_message()
    vote()
    tg.idle()


if __name__ == "__main__":
    main()
