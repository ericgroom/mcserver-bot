from collections import namedtuple
from bot.formatter import format_player_list

Player = namedtuple("Player", ["name"])

class StatusMock:
    def __init__(self, players, max=5):
        self.max = max
        if players:
            self.sample = [Player(name) for name in players]
            self.online = len(players)
        else:
            self.sample = None
            self.online = 0

def test_none_online():
    status = StatusMock(None)
    result = format_player_list(status)
    assert "nobody" in result

def test_one_online():
    status = StatusMock(["MrOSM"])
    result = format_player_list(status)
    assert "1" in result
    assert "MrOSM" in result