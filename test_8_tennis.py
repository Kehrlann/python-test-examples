from examples.tennis import Game


def test_no_points():
    game = Game()

    assert game.score() == "0:0"


def test_score_p1():
    game = Game()

    game.score_point(Game.p1)
    assert game.score() == "15:0"

    game.score_point(Game.p1)
    assert game.score() == "30:0"

    game.score_point(Game.p1)
    assert game.score() == "40:0"


def test_score_p2():
    game = Game()

    game.score_point(Game.p2)
    assert game.score() == "0:15"

    game.score_point(Game.p2)
    assert game.score() == "0:30"

    game.score_point(Game.p2)
    assert game.score() == "0:40"


def test_win_p2():
    game = Game()

    game.score_point(Game.p2)
    game.score_point(Game.p2)
    game.score_point(Game.p2)
    game.score_point(Game.p2)

    assert game.score() == "WIN P2"


def test_win_p1():
    game = Game()

    game.score_point(Game.p1)
    game.score_point(Game.p1)
    game.score_point(Game.p1)
    game.score_point(Game.p1)

    assert game.score() == "WIN P1"


def test_avantage():
    game = Game()

    game.score_point(Game.p1)
    game.score_point(Game.p1)
    game.score_point(Game.p1)
    game.score_point(Game.p2)
    game.score_point(Game.p2)
    game.score_point(Game.p2)

    game.score_point(Game.p1)

    assert game.score() == "Ad:40"


def test_avantage_go_back():
    game = Game()

    game.score_point(Game.p1)
    game.score_point(Game.p1)
    game.score_point(Game.p1)
    game.score_point(Game.p2)
    game.score_point(Game.p2)
    game.score_point(Game.p2)
    game.score_point(Game.p1)  # Ad:40

    game.score_point(Game.p2)

    assert game.score() == "40:40"
