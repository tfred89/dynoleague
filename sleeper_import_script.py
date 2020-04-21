import json
import requests

def sleeper_import():
    endpoint = "https://api.sleeper.app/v1/players/nfl"
    payload = requests.get(endpoint)
    data = json.loads(payload.text)
    with open('sleeper_data.txt', 'w') as outfile:
        json.dump(data, outfile)
    print('Write successfull')

sleeper_import()