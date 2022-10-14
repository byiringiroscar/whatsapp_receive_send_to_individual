import requests
from requests.exceptions import ConnectionError
from decouple import config

API_TOKEN = config('API_TOKEN')
INSTANCE = config('INSTANCE')


def get_all_chat_messages_individual():
    url = f"https://api.ultramsg.com/{INSTANCE}/chats"

    querystring = {"token": f"{API_TOKEN}"}

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        new_data = response.json()
        return new_data
    except ConnectionError as e:
        print(e)
        return False

