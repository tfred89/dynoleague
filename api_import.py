'''
Need import from 2 APIs: ESPN for league teams and Sleeper for players
'''
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RSWKsite.settings")

import django
django.setup()

from league.models import *
from ff_espn_api import League
import json

#  add teams/leagues from ESPN

def espn_update():
    year = 2020
    league_id = 935365 
    swid = '{CC3929FE-4B90-497B-87D7-6283A951436F}'
    espn_s2 = 'AECzc3DemsoJ5PyewWk65BE%2BWjxjuClSu%2FZJ2iTSvRw97IsbEqSe1qqMBq4KkyiVURjLO7Hrdm7kO0BZgbNWoW3CL%2BwD0ybo66ONErCT8paWqRjhRxv8MgHJZp0eVbJm6oIs4pyCqugJ9KwxuJX5J4iMXIXDDKzlXnJ%2FxxN0SUUWzZuDjv3snuqP45eY6fO5bmfz1ckweC2GFnL5xaWkoWL568GlkdbYoF2Hn9thzFHgB5B%2BCpftNvOs2vaPKEwVg9mUDjnj34ELOKfrAmSWSf49eOIJMp5BHe1VJroEe2VXgw%3D%3D'
    league = League(league_id, year, espn_s2, swid)
    # insert logic to add teams, owners, players?


def sleeper_import():
    # endpoint = "https://api.sleeper.app/v1/players/nfl"
    # payload = requests.get(endpoint)
    # data = json.dumps(payload)  # may need to be json.loads
    with open('sleeper_data.txt', 'r') as infile:
        sleeper_data = json.load(infile)
    for k,v in sleeper_data.items():
        y = player_import(v)
        


    '''
    iterate through and load results
    needed keys:
                'fantasy_positions'
                'weight'
                'position'
                'height'
                'age'
                'years_exp'
    '''
