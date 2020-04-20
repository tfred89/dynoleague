from django.shortcuts import render
from league.models import DraftPick, Owner
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

class DraftPickListView(ListView):

    model = DraftPick

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['draftpicks']


def league_rosters(request):
    owners_list = Owner.objects.all()
    context = {'owners':owners_list}

    return render(request, 'league/rosters.html', context)