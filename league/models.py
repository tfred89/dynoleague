from django.db import models
from django.db.models import Avg, Max, Min, StdDev, Sum


class Owner(models.Model):
    owner_name = models.CharField(max_length=100, unique=True, primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.owner_name



class PastSeasons(models.Model):
    year = models.IntegerField()
    place = models.IntegerField()
    team_name = models.CharField(max_length=100, unique=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    points_for = models.FloatField()
    points_against = models.FloatField()

    objects = models.Manager()
    stats = PastQS.as_manager()


    def __str__(self):
        return str(self.year)


class CurrentSeason(models.Model):
    year = models.IntegerField(blank=True, null=True)
    game_week = models.IntegerField()
    team_name = models.CharField(max_length=100, unique=False)
    team_abbrev = models.CharField(max_length=100, unique=False)
    points_for = models.FloatField() # changed from 'poinst', this may cause DB issues
    opponent = models.CharField(max_length=100, unique=False)
    points_against = models.FloatField()
    result = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    point_dif = models.FloatField(blank=True, null=True)


    @property
    def margin(self):
        dif = self.points_for - self.points_against
        return dif

    def __str__(self):
        return 'GW ' + str(self.game_week)

    class Meta:
        ordering = ['-year', 'game_week']

# Needed models to eliminate constant espn API calls:
# Goes with function api_functions.get_standings


class Rankings(models.Model):
    year = models.IntegerField()
    game_week = models.IntegerField()
    team_name = models.CharField(max_length=100, unique=False)
    team_abbrev = models.CharField(max_length=100, unique=False)
    points_for = models.FloatField()
    points_against = models.FloatField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    place = models.IntegerField()
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.place} place gw {self.game_week}"

    class Meta:
        ordering = ['game_week', 'place']


class NFLPlayer(models.Model):
    name = models.CharField(max_length=120)
    team = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    roster = models.ForeignKey('Assets', models.CASCADE, related_name='players')
    taxi = models.BooleanField(default=False)
    rostered = models.BooleanField(default=False)
    tenure = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.CharField(max_length=6)
    weight = models.IntegerField()


class DraftPick(models.Model):
    year = models.IntegerField()
    round = models.IntegerField()
    pick = models.IntegerField(blank=True, null=True)  # won't know until after lottery
    owner =  models.ForeignKey('Assets', models.CASCADE, related_name='picks')
    trade_history = models.CharField(max_length=140)  # Fix then, want entire chain of pick history

    ordering = ['year', 'round', 'pick']
    
    def history(self):
        return self.picktrade_set().all()  # is .all() needed?


class PickTrade(models.Model):
    pick = models.ForeignKey(DraftPick, models.CASCADE)
    traded_from = models.ForeignKey(Owner, models.CASCADE)
    traded_to = models.ForeignKey(Owner, models.CASCADE)
    date = models.DateField()  # default = 'now'


class Assets(models.Model):
    manager = models.OneToOneField(Owner, models.CASCADE, required=True)


class LeagueRules(models.Model):
    rule = models.TextField()

'''
Template access:

owner.assets.picks
owner.assets.players
'''