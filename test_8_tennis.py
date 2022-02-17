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


def test_scores():
    game = Game()

    game.score_point(Game.p1)
    assert game.score() == "15:0"

    game.score_point(Game.p2)
    assert game.score() == "15:15"

    game.score_point(Game.p2)
    assert game.score() == "15:30"

    game.score_point(Game.p1)
    assert game.score() == "30:30"

    game.score_point(Game.p1)
    assert game.score() == "40:30"

    game.score_point(Game.p2)
    assert game.score() == "40:40"