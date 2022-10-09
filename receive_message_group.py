from get_all_message import receive_message_sent
from convert_timestamp import convert_time_stamp
from datetime import datetime

now_date = datetime.now().date()


def receive_msg():
    all_message = receive_message_sent()
    message_new = []
    if not all_message:
        print("connection error ---------------")
        return False
    else:
        for all in all_message:
            time_sent = convert_time_stamp(all['timestamp']).date()
            if now_date == time_sent:
                message_new.append(all)
    return message_new

