from get_individual_chat import get_all_chat_messages_individual
from convert_timestamp import convert_time_stamp
from datetime import datetime

now_date = datetime.now().date()



def get_all_arranged_chat():
    all_chats_message = get_all_chat_messages_individual()
    all_chat_arranged = []
    if not all_chats_message:
        print("connection -----------error -------------")
        return False
    else:
        for chat in all_chats_message:
            if not chat['isGroup'] and chat['unread'] > 0:
                time_sent = convert_time_stamp(chat['last_time']).date()
                if now_date == time_sent:
                    all_chat_arranged.append(chat)
                    return all_chat_arranged
            else:
                return 'no-data'

# print(get_all_arranged_chat())
