import mysql.connector


def receive_db_message():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="whatsapp_send")

    mycursor = mydb.cursor()

    mycursor.execute("select * from messages_db")
    result = mycursor.fetchall()
    if result:
        for i in range(0, len(result)):
            if i == (len(result) - 1):
                return result[i][0]
    else:
        return 'no-data'



