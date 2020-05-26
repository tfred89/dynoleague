from league.models import NFLPlayer
import json
import requests


class PlayerUpdater:

    pos = ['WR', 'QB', 'TE', 'K', 'DEF']
    endpoint = "https://api.sleeper.app/v1/players/nfl"
    added = 0

    def __init__(self):
        self.api_data = json.loads(requests.get(self.endpoint).text)

    def update_player(self, data):
        position_list = data.get('fantasy_positions', [])
        if position_list and len(position_list) > 0:
            position = position_list[0]
        else:
            position = 'N'
        if position in self.pos:
            eid = str(data.get('espn_id'))
            sid = data.get('player_id')
            p_name = data.get('first_name')+' '+ data.get('last_name')
            p, c = NFLPlayer.objects.get_or_create(sleeper_id=sid)
            p.name=p_name
            p.team=data.get('team')
            p.position=data.get('position')
            p.tenure=data.get('years_exp')
            p.age=data.get('age')
            p.height=data.get('height')
            p.weight=data.get('weight')
            p.espn_id=eid
            p.sleeper_id=sid
            p.save()
            if c:
                self.added += 1
        else:
            pass

    def update(self):
        for v in self.api_data.values():
            self.update_player(v)
