from django.db import models
from django.db.models import Avg, Max, Min, StdDev, Sum


class Owner(models.Model):
    owner_name = models.CharField(max_length=100, unique=True, primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.owner_name


class FantasyTeam(models.Model):
    owner = models.ForeignKey(Owner, models.CASCADE, related_name='team')
    abbrev = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    division = models.IntegerField()


class PastSeason(models.Model):
    year = models.IntegerField()
    place = models.IntegerField()
    team_name = models.CharField(max_length=100, unique=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='history')
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    points_for = models.FloatField()
    points_against = models.FloatField()

    class Meta:
        ordering = ['year', 'place']

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
    name = models.CharField(max_length=120, blank=True, null=True)
    team = models.CharField(max_length=120, blank=True, null=True)
    position = models.CharField(max_length=120, blank=True, null=True)
    roster = models.ForeignKey('Assets', models.CASCADE, related_name='players', blank=True, null=True)
    taxi = models.BooleanField(default=False)
    rostered = models.BooleanField(default=False)
    tenure = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.CharField(max_length=8, blank=True, null=True)
    weight = models.CharField(max_length=8, blank=True, null=True)
    espn_id = models.CharField(max_length=125, blank=True, null=True)
    sleeper_id = models.CharField(max_length=125, blank=True, null=True)


    class Meta:
        ordering = ['position', '-tenure']


class DraftPick(models.Model):
    year = models.IntegerField()
    round = models.IntegerField()
    pick = models.IntegerField(blank=True, null=True)  # won't know until after lottery
    owner =  models.ForeignKey('Assets', models.CASCADE, related_name='picks', blank=True, null=True)
 # Fix then, want entire chain of pick history

    class Meta:
        ordering = ['year', 'round', 'pick']

    def __str__(self):
        if self.pick:
            return f"{self.year} Rd {self.round}.{self.pick}"
        else:
            return f"{self.year} Rd {self.round}"
    
    # def history(self):
    #     return self.picktrade_set().all()  # is .all() needed?


class PickTrade(models.Model):
    pick = models.ForeignKey(DraftPick, models.CASCADE)
    traded_from = models.ForeignKey(Owner, models.CASCADE, related_name='pick_from')
    traded_to = models.ForeignKey(Owner, models.CASCADE, related_name='pick_to')
    date = models.DateField()  # default = 'now'


class Assets(models.Model):
    manager = models.OneToOneField(Owner, models.CASCADE)

    def __str__(self):
        return self.manager.owner_name


class LeagueRules(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=127)
    rule = models.TextField()


class RuleProposal(models.Model):
    number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=127)
    proposal = models.TextField()

    class Meta:
        ordering = ['number',]

    def __str__(self):
        return self.name


class Dates(models.Model):
    name = models.CharField(max_length=65)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    

