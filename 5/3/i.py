# I. Играйте в футбол!

from sys import stdin
from re import search
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass(init=False)
class Goal:
    player: str
    time: int

    def __init__(self, s: str) -> None:
        m = search(r"(?P<player>.+)\s+(?P<t>\d+)'", s)
        if m is None:
            raise ValueError
        self.player = m['player']
        self.time = int(m['t'])


@dataclass
class Player:
    team: 'Team'
    goals: int = 0
    minutes: list[str] = field(default_factory=lambda: [0] * 91)
    opened: int = 0

    def add_goal(self, t: int):
        self.minutes[t] += 1
        self.goals += 1

    def on_minute(self, t: int) -> int:
        return self.minutes[t]

    def on_first(self, t: int) -> int:
        goals = (self.minutes[i] for i in range(1, t + 1))
        return sum(goals)

    def on_last(self, t: int) -> int:
        goals = (self.minutes[i] for i in range(91 - t, 91))
        return sum(goals)

    @property
    def mean(self) -> float:
        return float(self.goals / self.team.games)


@dataclass
class Team:
    games: int = 0
    players: dict[str, Player] = field(default_factory=dict)

    def add_goals(self, goals: list[Goal]):
        self.games += 1
        for goal in goals:
            if goal.player not in self.players:
                self.players[goal.player] = Player(team=self)
            self.players[goal.player].add_goal(goal.time)


    def get_player(self, player: str) -> Player | None:
        if player in self.players:
            return self.players[player]
        return None

    @staticmethod
    def who_opened(team1: str, goals1: list[Goal], team2: str, goals2: list[Goal]) -> tuple[str, str, int]:
        if goals1 and (not goals2 or goals1[0].time < goals2[0].time):
            return team1, goals1[0].player, goals1[0].time
        if goals2 and (not goals1 or goals2[0].time < goals1[0].time):
            return team2, goals2[0].player, goals2[0].time
        return '', '', 0

    @property
    def mean(self) -> float:
        return float(self.goals / self.games)

    @property
    def opened(self) -> int:
       opened = (player.opened for player in self.players.values())
       return sum(opened)

    @property
    def goals(self) -> int:
        goals = (player.goals for player in self.players.values())
        return sum(goals)


def find_player(teams: list[Team], player: str) -> Player | None:
    for team in teams:
        p = teams[team].get_player(player)
        if p:
            return p
    return Player(team=None)


teams = defaultdict(Team)

for line in stdin:
    if m := search(r'"(?P<team1>.+)" \- "(?P<team2>.+)" (?P<g1>\d+):(?P<g2>\d+)', line):
        team1 = m['team1']
        g1 = int(m['g1'])
        goals1 = [Goal(stdin.readline()) for _ in range(g1)]
        teams[team1].add_goals(goals1)

        team2 = m['team2']
        g2 = int(m['g2'])
        goals2 = [Goal(stdin.readline()) for _ in range(g2)]
        teams[team2].add_goals(goals2)

        team, player, t = Team.who_opened(team1, goals1, team2, goals2)
        if team:
            teams[team].players[player].opened += 1

    elif m := search(r'Total goals for "(?P<t>.+)"', line):
        t = m['t']
        print(teams[t].goals)
    elif m := search(r'Mean goals per game for "(?P<t>.+)"', line):
        t = m['t']
        print(teams[t].mean)
    elif m := search(r'Total goals by (?P<p>.+)', line):
        p = find_player(teams, m['p'])
        print(p.goals)
    elif m := search(r'Mean goals per game by (?P<p>.+)', line):
        p = find_player(teams, m['p'])
        print(p.mean)
    elif m := search(r'Goals on minute (?P<t>\d+) by (?P<p>.+)', line):
        t = int(m['t'])
        p = find_player(teams, m['p'])
        print(p.on_minute(t))
    elif m := search(r'Goals on first (?P<t>\d+) minutes by (?P<p>.+)', line):
        t = int(m['t'])
        p = find_player(teams, m['p'])
        print(p.on_first(t))
    elif m := search(r'Goals on last (?P<t>\d+) minutes by (?P<p>.+)', line):
        t = int(m['t'])
        p = find_player(teams, m['p'])
        print(p.on_last(t))
    elif m := search(r'Score opens by "(?P<t>.+)"', line):
        print(teams[m['t']].opened)
    elif m := search(r'Score opens by (?P<p>.+)', line):
        p = find_player(teams, m['p'])
        print(p.opened)
    else:
        raise ValueError
