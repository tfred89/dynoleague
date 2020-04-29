from django.shortcuts import render
from league.models import DraftPick, Owner, LeagueRules
from django.views.generic.list import ListView
# Create your views here.
'''
needs:
view displaying tables of:
-- owner roster
-- owner taxi taxi_squad
-- owner picks

-- draft order with owner next to order
-- rules page

questions:
best way/package to provide tables (preferably sortable)

'''

def draft_pick_list(request):
    picks = DraftPick.objects.filter(year=2020)
    
    context = {
        'round1': picks.filter(round=1),
        'round2': picks.filter(round=2),
        'round3': picks.filter(round=3),
        'round4': picks.filter(round=4),
        'round5': picks.filter(round=5)
        }
    return render(request, 'league/draftpick_list.html', context)


def league_rosters(request):
    owners_list = Owner.objects.all()
    context = {'owners':owners_list}

    return render(request, 'league/rosters.html', context)

def home(request):
    return render(request, 'league/home.html')


def league_rules(request):
    rule_list = LeagueRules.objects.all()
    context = {'rules':rule_list}
    return render(request, 'league/rules.html', context)