from dataclasses import dataclass


@dataclass
class Player:
    score: int = 0

class Game:
    p1 = 1
    p2 = 2

    __scores = ["0", "15", "30", "40"]

    def __init__(self):
        self.score_1 = 0
        self.score_2 = 0

    def score_point(self, player):
        if player == Game.p1:
            self.score_1 += 1
        elif player == Game.p2:
            self.score_2 += 1

    def score(self):
        return f"{self.__scores[self.score_1]}:{self.__scores[self.score_2]}"
