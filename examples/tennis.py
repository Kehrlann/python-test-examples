class Game:

    __scores = ["0", "15", "30", "40", "Ad"]

    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def p1_score_point(self):
        if self.p1_score > 3 and self.p2_score - self.p1_score == 1:
            self.p2_score -= 1
        if self.p1_score == 3 and not self.__is_40A():
            self.p1_score += 2
        else:
            self.p1_score += 1

    def p2_score_point(self):
        if self.p1_score > 3 and self.p1_score - self.p2_score == 1:
            self.p1_score -= 1
        elif self.p2_score == 3 and not self.__is_40A():
            self.p2_score += 2
        else:
            self.p2_score += 1

    def __is_40A(self):
        return self.p1_score == self.p2_score == 3

    def score(self):
        if self.p2_score >= len(self.__scores):
            return "WIN P2"
        elif self.p1_score >= len(self.__scores):
            return "WIN P1"
        return f"{self.__scores[self.p1_score]}:{self.__scores[self.p2_score]}"
