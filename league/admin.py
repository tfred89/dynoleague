from django.contrib import admin
from league.models import *


# class RankingsA(admin.ModelAdmin):
#     list_display = ['year', 'game_week', 'team_name', 'owner',
#                     'place', 'wins', 'losses']
#     search_fields = ['game_week',]
#     list_filter = ('game_week', 'team_name', 'place',)


# class PastSeasonsA(admin.ModelAdmin):
#     list_display = ['year', 'place', 'team_name',
#                     'owner', 'wins', 'losses', 'ties']
#     search_fields = ['owner', 'year']
#     list_filter = ('year', 'place', 'owner',)


# class CSA(admin.ModelAdmin):
#     list_display = ['year', 'game_week', 'team_name', 'points_for',
#                     'points_against', 'owner', 'point_dif']
#     search_fields = ['owner', 'team_name']

class PickManager(admin.ModelAdmin):
    list_display = ['round', 'pick', 'year', 'owner']


class RuleManager(admin.ModelAdmin):
    list_display = ['number', 'title']


class PlayerManager(admin.ModelAdmin):
    list_display = ['name', 'team', 'position', 'rostered']
    search_fields = ['name', 'team', 'position']
    list_filter = ['team', 'position', 'rostered']


class PastManager(admin.ModelAdmin):
    list_display = ['year', 'owner']


class DateManager(admin.ModelAdmin):
    list_display = ['name', 'date']

# Register your models here.
admin.site.register(PastSeason, PastManager)
admin.site.register(CurrentSeason)
admin.site.register(NFLPlayer, PlayerManager)
admin.site.register(Rankings)
admin.site.register(Owner)
admin.site.register(DraftPick, PickManager)
admin.site.register(PickTrade)
admin.site.register(Assets)
admin.site.register(LeagueRules, RuleManager)
admin.site.register(RuleProposal)
admin.site.register(Dates, DateManager)
