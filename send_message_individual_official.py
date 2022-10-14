from receive_individual_chat_process import get_all_arranged_chat
from receive_message_individiual_by_id import receive_message_sent
import mysql.connector
from convert_timestamp import convert_time_stamp
from convert_phone import get_absolute_phone_number
from send_message_to_user import send_message_to_individual
from check_message_word import check_message_contain


all_chat_message = get_all_arranged_chat()

if not all_chat_message:
    print(all_chat_message)
    print("connection --------------error ----------- occurred ------------")
elif all_chat_message == 'no-data':
    print("no ------------specifies ------data----------")
else:
    if all_chat_message:
        for chat in all_chat_message:
            chat_unread = chat['unread']
            message_specified = receive_message_sent(chat['id'])[-chat_unread:]
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="whatsapp_send")

            mycursor = mydb.cursor()

            mycursor.execute("select * from receive_send_message_individual")
            result = mycursor.fetchall()
            if result:
                for received_msg in message_specified:
                    try:
                        if check_message_contain((received_msg['body']).lower()):
                            sql = "INSERT INTO receive_send_message_individual (id, message_body, time_sent, phone_number, Identifier) VALUES (%s, %s, %s, %s,%s)"
                            time_sent_exact = convert_time_stamp(received_msg['timestamp'])
                            sender_phone_number = get_absolute_phone_number(received_msg['from'])
                            val = (received_msg['id'], received_msg['body'], time_sent_exact, sender_phone_number, 0)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print(mycursor.rowcount, "record inserted.")
                            # send msg
                            try:
                                send_message_to_individual(received_msg['from'])
                            except:
                                print("something went wrong -----")
                        else:
                            print("============keyword=====not =====found")
                    except:
                        print("record already in db")
            else:
                for received_msg in message_specified:
                    try:
                        if check_message_contain((received_msg['body']).lower()):
                            sql = "INSERT INTO receive_send_message_individual (id, message_body, time_sent, phone_number, Identifier) VALUES (%s, %s, %s, %s,%s)"
                            time_sent_exact = convert_time_stamp(received_msg['timestamp'])
                            sender_phone_number = get_absolute_phone_number(received_msg['from'])
                            val = (received_msg['id'], received_msg['body'], time_sent_exact, sender_phone_number, 0)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print(mycursor.rowcount, "record inserted.")
                            # send msg
                            try:
                                send_message_to_individual(received_msg['from'])
                            except:
                                print("something went wrong -----")
                        else:
                            print("============keyword=====not =====found")
                    except:
                        print("record already in db")
    else:
        print("message --------------is---------------empty")


