import requests
from requests.exceptions import ConnectionError
from decouple import config
from get_db_message import receive_db_message

API_TOKEN = config('API_TOKEN')
INSTANCE = config('INSTANCE')





def send_message_to_individual(WHATSAPP_ID):

    if WHATSAPP_ID == '':
        print("no ----author----")
    else:
        message_reply = receive_db_message()
        if message_reply == 'no-data':
            print("no ------message---to----be---sent---in ---table")
        else:
            message_body = message_reply
            url = f"https://api.ultramsg.com/{INSTANCE}/messages/chat"

            payload = f"token={API_TOKEN}&to={WHATSAPP_ID}&body={message_body}&priority=1&referenceId="
            headers = {'content-type': 'application/x-www-form-urlencoded'}

            try:
                response = requests.request("POST", url, data=payload, headers=headers)
                return response.text
            except ConnectionError as e:
                print(e)
                return False



