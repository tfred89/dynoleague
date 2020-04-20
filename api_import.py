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
    league_id = 1406490  # fix
    swid = '{CC3929FE-4B90-497B-87D7-6283A951436F}'  # fix
    espn_s2 = 'AECMpoZv%2FZF6G9Q1PEU9bnJD2Xf8FJwcFa8voarn81ZyGsMy8BzOpN8M6Wd9dLle3mHCQpW%2F0uQja23BYQagdA9H6tFSbtqGyyg%2BZs3m22Y%2FKNxo7os%2BBNSjX4bKa6UOSBlOph7KwtyMFBe654mVtR4inWzGYrTFVo2RIDk6ueNPFnz%2BDlKaxcQhRniwrEnXhprLfL78Gel1JetARL5lkiqGR2f%2BaPoxq%2Btfb8uj%2BzQAkMEkwJZaoWOUCPfxa7w%2FLa5GVnX5Ca%2F2ZqhFeysjWwOhYflDFnlItB1SKjpWPFtQ2w%3D%3D'  # fix
    league = League(league_id, year, espn_s2, swid)
    # insert logic to add teams


def sleeper_import():
    endpoint = "https://api.sleeper.app/v1/players/nfl"
    payload = requests.get(endpoint)
    data = json.dumps(payload)  # may need to be json.loads
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
