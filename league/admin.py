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




# Register your models here.
admin.site.register(PastSeason)
admin.site.register(CurrentSeason)
admin.site.register(NFLPlayer)
admin.site.register(Rankings)
admin.site.register(Owner)
admin.site.register(DraftPick, PickManager)
admin.site.register(PickTrade)
admin.site.register(Assets)
admin.site.register(LeagueRules)
admin.site.register(RuleProposal)
admin.site.register(Dates)
