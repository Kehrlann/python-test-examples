from dataclasses import dataclass


@dataclass
class Player:
    score: int = 0

class Game:
    p1 = 1
    p2 = 2

    __scores = ["0", "15", "30", "40", "Ad"]

    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()

    def score_point(self, player):
        if player == Game.p1:
            player = self.p1
            other = self.p2
        elif player == Game.p2:
            player = self.p2
            other = self.p1

        if other.score > 3 and other.score - player.score == 1:
            other.score -= 1
        elif player.score == 3 and not self.__is_40A():
            player.score += 2
        else:
            player.score += 1

    def __is_40A(self):
        return self.p1.score == self.p2.score == 3

    def score(self):
        if self.p2.score >= len(self.__scores):
            return "WIN P2"
        elif self.p1.score >= len(self.__scores):
            return "WIN P1"
        return f"{self.__scores[self.p1.score]}:{self.__scores[self.p2.score]}"
