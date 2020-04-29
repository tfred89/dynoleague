import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynoleague.settings")

import django
django.setup()

'''
Past seasons data import from ESPN:

 'division_id',
 'final_standing',
 'get_player_name',
 'logo_url',
 'losses',
 'mov',
 'outcomes',
 'owner',
 'points_against',
 'points_for',
 'roster',
 'schedule',
 'scores',
 'standing',
 'streak_length',
 'streak_type',
 'team_abbrev',
 'team_id',
 'team_name',
 'wins'


 class PastSeason(models.Model):
 y   year = models.IntegerField()
 y   place = models.IntegerField()
 y   team_name = models.CharField(max_length=100, unique=False)
 y   owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
 y   wins = models.IntegerField()
 y   losses = models.IntegerField()
 n   ties = models.IntegerField()
 y   points_for = models.FloatField()
 y   points_against = models.FloatField()


    def __str__(self):
        return str(self.year)

___
Iterate through each year
iterate through each team ignoring fakes
add record for each team
'''
from league.models import PastSeason, Owner
from ff_espn_api import League


def get_league(year):
    league_id = 935365 
    swid = '{CC3929FE-4B90-497B-87D7-6283A951436F}'
    espn_s2 = 'AECzc3DemsoJ5PyewWk65BE%2BWjxjuClSu%2FZJ2iTSvRw97IsbEqSe1qqMBq4KkyiVURjLO7Hrdm7kO0BZgbNWoW3CL%2BwD0ybo66ONErCT8paWqRjhRxv8MgHJZp0eVbJm6oIs4pyCqugJ9KwxuJX5J4iMXIXDDKzlXnJ%2FxxN0SUUWzZuDjv3snuqP45eY6fO5bmfz1ckweC2GFnL5xaWkoWL568GlkdbYoF2Hn9thzFHgB5B%2BCpftNvOs2vaPKEwVg9mUDjnj34ELOKfrAmSWSf49eOIJMp5BHe1VJroEe2VXgw%3D%3D'
    league = League(league_id, year, espn_s2, swid)
    return league

def add_record(year, obj):
    owner = Owner.objects.get(owner_id=obj.get('team_id'))
    r, created = PastSeason.objects.get_or_create(
        year=year,
        place = obj.get('final_standing'),
        team_name = obj.get('team_name'),
        owner = owner,
        wins = obj.get('wins'),
        losses = obj.get('losses'),
        ties = 0,
        points_for = obj.get('points_for'),
        points_against = obj.get('points_against'),
    )
    if created:
        print(f'{owner.owner_name} record for {year} season added')
    return created

def start_import():
    szn = [2017, 2018, 2019]
    count = 0
    ignore = ['Team 11', 'Team 12', 'Team 13', 'Team 14']
    for year in szn:
        league = get_league(year)
        for team in league.teams:
            if team.team_name not in ignore:
                
                c = add_record(year, team.__dict__)
                if c:
                    count += 1
                    print(f'{count} records have been added')
    print(f'{count} total records added')

if __name__ == '__main__':
    start_import()
    print(' SCRIPT COMPLETED ')