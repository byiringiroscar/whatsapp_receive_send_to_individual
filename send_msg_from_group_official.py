from receive_message_group import receive_msg
import mysql.connector
from convert_timestamp import convert_time_stamp
from convert_phone import get_absolute_phone_number
from send_message_to_user import send_message_to_individual
from check_message_word import check_message_contain

all_message_group = receive_msg()


if not all_message_group:
    print("----connection ------error -------- or--------no ----data----returned--")
elif all_message_group == 'no-data':
    print("no -----data----returned----specified")

else:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="whatsapp_send")

    mycursor = mydb.cursor()

    mycursor.execute("select * from receive_send_message_group")
    result = mycursor.fetchall()
    if result:

        for received_msg in all_message_group:
            for message in result:
                try:
                    if check_message_contain((received_msg['body']).lower()):
                        sql = "INSERT INTO receive_send_message_group (id, message_body, time_sent, phone_number, Identifier) VALUES (%s, %s, %s, %s,%s)"
                        time_sent_exact = convert_time_stamp(received_msg['timestamp'])
                        sender_phone_number = get_absolute_phone_number(received_msg['author'])
                        val = (received_msg['id'], received_msg['body'], time_sent_exact, sender_phone_number, 0)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")
                        #send msg
                        try:
                            send_message_to_individual(received_msg['author'])
                        except:
                            print("something went wrong -----")
                    else:
                        print("============keyword=====not =====found")
                except:
                    print("record already in db")

    else:
        for received_msg in all_message_group:
            try:
                if check_message_contain((received_msg['body']).lower()):
                    sql = "INSERT INTO receive_send_message_group (id, message_body, time_sent, phone_number, Identifier) VALUES (%s, %s, %s, %s,%s)"
                    time_sent_exact = convert_time_stamp(received_msg['timestamp'])
                    sender_phone_number = get_absolute_phone_number(received_msg['author'])
                    val = (received_msg['id'], received_msg['body'], time_sent_exact, sender_phone_number)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")
                    try:
                        send_message_to_individual(received_msg['author'])
                    except:
                        print("something went wrong -----")
                else:
                    print("============keyword=====not =====found")
            except:
                print("record already in db")

