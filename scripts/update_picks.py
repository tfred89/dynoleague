import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynoleague.settings")

import django
django.setup()

from league.models import DraftPick, Owner

def create_pick(yr, rd, pk, known):
    if known:
        p, c = DraftPick.objects.get_or_create(
            year=yr,
            round=rd,
            pick=pk
        )
    else:
        p, c = DraftPick.objects.get_or_create(
            year=yr,
            round=rd
        ) 
    if c:
        print(f'{yr} pick {rd} has been added')

def create_year(yr, known):
    for rd in range(1,6):
        for pk in range(1,11):
            create_pick(yr, rd, pk, known)


def future_picks():
    owners = Owner.objects.all()
    for o in owners:
        assets = o.assets
        for rd in range(1,6):
            p, c = DraftPick.objects.get_or_create(
                year=2022,
                round=rd,
                owner=assets,
            )
        print(f'round {rd} pick created')


if __name__ == '__main__':
    # create_year(2019, True)
    # create_year(2022, False)
    future_picks()