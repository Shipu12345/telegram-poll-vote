import time
from telegram.client import Telegram
import os
import json

VOTER_COUNT_THRESHOLD = 7


tg = Telegram(
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    phone=os.getenv("PHONE"),
    database_encryption_key="changeme1234",
)


def delete_line_from_file(chat_id, msg_id):
    with open("temp/polls.txt", "r") as f:
        lines = f.readlines()
    with open("temp/polls.txt", "w") as f:
        for line in lines:
            if chat_id not in line.strip("\n") and msg_id not in line.strip("\n"):
                f.write(line)


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


def get_message(chat_id, message_id):
    result = tg.get_message(chat_id, message_id)
    result.wait()

    if result.error:
        print(f"get history error: {result.error_info}")
    else:
        message_content = result.update["content"]
        print("message Content", message_content)
        return message_content


def get_optimal_option(options: list):
    max_count = 0
    optimal_option_index = 0
    is_updated = False
    for i, option in enumerate(options):
        if option["is_chosen"]:
                is_updated = True
        if option["voter_count"] > max_count:
            max_count = option["voter_count"]
            optimal_option_index = i

    return optimal_option_index, is_updated


#  Sir Asad's Telegram-Poll Algo:: Let A Telegram Poll, IFF designed by Sofian (blonde), the Count of votes of an option is directly proportional to the probability the optimal voting option.
#  vote_count: R ~ P(O(answer)): R

def sir_asad_algorithm(update):

    # Reading existing polls
    with open("temp/polls.txt", "r+") as file:
        polls_list = file.readlines()

    for param in polls_list:
        param = json.loads(param)
        time.sleep(5)
        
        message_content = get_message(param["chat_id"], param["message_id"])
        if not message_content["poll"]["is_closed"]:
            voter_count = message_content["poll"]["total_voter_count"]
            print("voter_count:", voter_count)
            if voter_count >= VOTER_COUNT_THRESHOLD:
                is_updated = False
                optimal_option_index, is_updated = get_optimal_option(
                    message_content["poll"]["options"]
                )
                param["option_ids"] = [optimal_option_index]
                vote(param, is_updated)

        # print(res.update)
        # print(res.messages)
    return True


def vote(params: dict, is_updated: bool = False):
    result = tg.call_method("setPollAnswer", params)
    result.wait()

    if result.error:
        print(f"send message error: {result.error_info}")
    else:
        print(f"message has been sent: {result.update}")
        if is_updated:
            delete_line_from_file(str(params['chat_id']), str(params['message_id']))
            is_updated = False
        
            

    


def new_message_handler(update):
    message_content = update["message"]["content"]

    print(message_content)
    # chat_id = os.getenv("GROUP_ID")
    message_text = message_content.get("text", {}).get("text", "").lower()

    if message_content["@type"] == "messagePoll":
        # time.sleep(500)
        # if not chat_id:
        #     chat_id = update['message']['chat_id']
        chat_id = update["message"]["chat_id"]
        params = {
            "chat_id": chat_id,
            "message_id": update["message"]["id"],
            "option_ids": [0],
        }
        print(f"Ping has been received from {chat_id}")
        try:
            with open("temp/polls.txt", "a") as file:
                file.writelines(json.dumps(params))

        except Exception as e:
            print(e)


def main():
    tg.login()
    # get_all_chats()
    # get_history()
    # # get_message()
    # vote(chat_id, msg_id)
    tg.add_message_handler(new_message_handler)
    tg.add_message_handler(sir_asad_algorithm)
    tg.idle()


if __name__ == "__main__":
    main()
