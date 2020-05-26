from django.shortcuts import render
from league.models import DraftPick, Owner, LeagueRules, Dates, RuleProposal
from django.views.generic.list import ListView
from league.utils import PlayerUpdater
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
    picks21 = DraftPick.objects.filter(year=2021)
    picks22 = DraftPick.objects.filter(year=2022)
    context = {
        'round1': picks.filter(round=1),
        'round2': picks.filter(round=2),
        'round3': picks.filter(round=3),
        'round4': picks.filter(round=4),
        'round5': picks.filter(round=5),
        'p21': picks21,
        'p22': picks22,
        }
    return render(request, 'league/draftpick_list.html', context)


def league_rosters(request):
    owners_list = Owner.objects.all()
    context = {'owners':owners_list}

    return render(request, 'league/rosters.html', context)


def home(request):
    dates = Dates.objects.all()
    new_rules = RuleProposal.objects.all()
    owners = Owner.objects.all()
    context = {
        'dates':dates,
        'props': new_rules,
        'owners': owners,
    }
    return render(request, 'league/home.html', context)


def history(request):
    owners = Owner.objects.all()
    context = {
        'owners':owners
    }
    return render(request, 'league/history.html', context)


def league_rules(request):
    rule_list = LeagueRules.objects.all()
    context = {'rules':rule_list}
    return render(request, 'league/rules.html', context)


def update_players_view(request):
    # if request.GET.get('mybtn'):
    upd = PlayerUpdater()
    upd.update()
    return render(request, 'league/update.html')