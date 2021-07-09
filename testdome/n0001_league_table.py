from collections import Counter
from collections import OrderedDict
from itertools import groupby
from operator import itemgetter


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]["games_played"] += 1
        self.standings[player]["score"] += score

    def player_rank(self, rank):
        # num, score, games_played
        standings = [
            (j[0], j[1]["score"], j[1]["games_played"], i)
            for i, j in enumerate(self.standings.items())
        ]
        sorted_by_score = sorted(standings, key=itemgetter(1), reverse=True)

        groups = groupby(sorted_by_score, key=itemgetter(1))

        result = []
        for k, g in groups:
            for i in sorted(g, key=itemgetter(2, 3)):
                result.append(i)

        return result[rank-1][0]


if __name__ == "__main__":
    table = LeagueTable(["Mike", "Chris", "Arnold"])
    table.record_result("Mike", 2)
    table.record_result("Mike", 3)
    table.record_result("Arnold", 5)
    table.record_result("Chris", 5)
    print(table.player_rank(1))
