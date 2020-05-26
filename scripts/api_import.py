
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynoleague.settings")

import django
django.setup()

from league.models import Owner, NFLPlayer, DraftPick
from ff_espn_api import League
import json
import requests

#  add teams/leagues from ESPN

def add_owner(name, id):
    p, created = Owner.objects.get_or_create(
        owner_name=name,
        owner_id=id,
    )
    return created


def espn_update():
    ignore = ['Team 11', 'Team 12', 'Team 13', 'Team 14']
    year = 2020
    league_id = 935365 
    swid = '{CC3929FE-4B90-497B-87D7-6283A951436F}'
    espn_s2 = 'AECzc3DemsoJ5PyewWk65BE%2BWjxjuClSu%2FZJ2iTSvRw97IsbEqSe1qqMBq4KkyiVURjLO7Hrdm7kO0BZgbNWoW3CL%2BwD0ybo66ONErCT8paWqRjhRxv8MgHJZp0eVbJm6oIs4pyCqugJ9KwxuJX5J4iMXIXDDKzlXnJ%2FxxN0SUUWzZuDjv3snuqP45eY6fO5bmfz1ckweC2GFnL5xaWkoWL568GlkdbYoF2Hn9thzFHgB5B%2BCpftNvOs2vaPKEwVg9mUDjnj34ELOKfrAmSWSf49eOIJMp5BHe1VJroEe2VXgw%3D%3D'
    league = League(league_id, year, espn_s2, swid)
    count = 0
    print('Owner database addition starting...')
    for team in league.teams:
        if team.team_name not in ignore:
            c = add_owner(team.owner, team.team_id)
            if c:
                count += 1
                print(f'Onwer {count} added')
    print(f'Owner update complete, {count} owners added')


def player_import(data):
    p_name = data.get('first_name')+' '+ data.get('last_name')
    eid = str(data.get('espn_id'))
    p, created = NFLPlayer.objects.get_or_create(
        name=p_name,
        team=data.get('team'),
        position=data.get('position'),
        tenure=data.get('years_exp'),
        age=data.get('age'),
        height=data.get('height'),
        weight=data.get('weight'),
        espn_id=eid,
        sleeper_id=data.get('player_id'),
    )
    return created

def sleeper_import():
    # endpoint = "https://api.sleeper.app/v1/players/nfl"
    # payload = requests.get(endpoint)
    # data = json.loads(payload)  # may need to be json.loads
    with open('sleeper_data.txt', 'r') as infile:
        sleeper_data = json.load(infile)
    count = 0
    print('Player import beginning')
    for v in sleeper_data.values():
        complete = player_import(v)
        if complete:
            count += 1
            print(f'player {count} added')
    print(f'sleeper player import completed. {count} players added to database')
        

def add_picks():
    rd = 6
    pk = 11
    for i in range(1, rd):
        for p in range(1, pk):
            new, created = DraftPick.objects.get_or_create(
                year=2020,
                round=i,
                pick=p,
            )
    for i in range(1, rd):
        for p in range(1, pk):
            new, created = DraftPick.objects.get_or_create(
                year=2021,
                round=i,
            )
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

def player_update(data: dict):
    pos = ['WR', 'QB', 'TE', 'K', 'DEF']
    position = data.get('fantasy_positions', ['N'])[0]
    if position in pos:
        eid = str(data.get('espn_id'))
        p_name = data.get('first_name')+' '+ data.get('last_name')
        p, c = NFLPlayer.objects.get_or_create(espn_id=eid)
        p.name=p_name
        p.team=data.get('team')
        p.position=data.get('position')
        p.tenure=data.get('years_exp')
        p.age=data.get('age')
        p.height=data.get('height')
        p.weight=data.get('weight')
        p.espn_id=eid
        p.sleeper_id=data.get('player_id')
        p.save()
    else:
        pass

if __name__ == '__main__':
    sleeper_import()
    espn_update()
    add_picks()
    print(' SCRIPT COMPLETED ')


