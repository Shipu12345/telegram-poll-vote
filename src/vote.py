import time
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


def vote(chat_id, msg_id):
    params = {
        "chat_id": chat_id,
        "message_id": msg_id,
        "option_ids": [0],
    }
    result = tg.call_method("setPollAnswer", params)
    result.wait()

    if result.error:
        print(f"send message error: {result.error_info}")
    else:
        print(f"message has been sent: {result.update}")

def new_message_handler(update):
        message_content = update['message']['content']
        print(message_content)
        chat_id = os.getenv("GROUP_ID")
        message_text = message_content.get('text', {}).get('text', '').lower()

        if message_content['@type'] == 'messagePoll':
            time.sleep(500)
            chat_id = update['message']['chat_id']
            print(f'Ping has been received from {chat_id}')
            try:
                vote(chat_id, update['message']['id'])
            except Exception as e:
                print(e)


def main():
    tg.login()
    # get_all_chats()
    # get_history()
    # # get_message()
    # vote(chat_id, msg_id)
    tg.add_message_handler(new_message_handler)
    tg.idle()


if __name__ == "__main__":
    main()
