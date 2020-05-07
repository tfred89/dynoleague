import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynoleague.settings")

import django
django.setup()

from league.models import Owner, NFLPlayer
from ff_espn_api import League
import json
import requests

def build_roster():
    ignore = ['Team 11', 'Team 12', 'Team 13', 'Team 14']
    year = 2020
    league_id = 935365 
    swid = '{CC3929FE-4B90-497B-87D7-6283A951436F}'
    espn_s2 = 'AECzc3DemsoJ5PyewWk65BE%2BWjxjuClSu%2FZJ2iTSvRw97IsbEqSe1qqMBq4KkyiVURjLO7Hrdm7kO0BZgbNWoW3CL%2BwD0ybo66ONErCT8paWqRjhRxv8MgHJZp0eVbJm6oIs4pyCqugJ9KwxuJX5J4iMXIXDDKzlXnJ%2FxxN0SUUWzZuDjv3snuqP45eY6fO5bmfz1ckweC2GFnL5xaWkoWL568GlkdbYoF2Hn9thzFHgB5B%2BCpftNvOs2vaPKEwVg9mUDjnj34ELOKfrAmSWSf49eOIJMp5BHe1VJroEe2VXgw%3D%3D'
    league = League(league_id, year, espn_s2, swid)
    count = 0
    for team in league.teams:
        if team.team_name not in ignore:
            owner = Owner.objects.get(owner_name=team.owner)
            for p in team.roster:
                pid = str(p.playerId)
                try:
                    player = NFLPlayer.objects.get(espn_id=pid)
                    player.roster = owner.assets
                    player.rostered = True
                    player.save()
                    count += 1
                    print(f"{player.name} added to {team.owner}'s roster")
                except:
                    pass
    print(f'{count} players added to rosters')

if __name__ == '__main__':
    build_roster()
    print(' SCRIPT COMPLETED ')