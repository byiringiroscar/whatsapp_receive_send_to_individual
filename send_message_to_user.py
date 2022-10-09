import requests
from decouple import config

API_TOKEN = config('API_TOKEN')
INSTANCE = config('INSTANCE')


def send_message_to_individual(WHATSAPP_ID):
    if WHATSAPP_ID == '':
        print("no ----author----")
    else:
        message_body = "it's done testing 911 "
        url = f"https://api.ultramsg.com/{INSTANCE}/messages/chat"

        payload = f"token={API_TOKEN}&to={WHATSAPP_ID}&body={message_body}&priority=1&referenceId="
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, data=payload, headers=headers)


