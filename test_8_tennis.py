from examples.tennis import Game


def test_no_points():
    game = Game()

    assert game.score() == "0:0"


def test_score_p1():
    game = Game()

    game.p1_score_point()
    assert game.score() == "15:0"

    game.p1_score_point()
    assert game.score() == "30:0"

    game.p1_score_point()
    assert game.score() == "40:0"


def test_score_p2():
    game = Game()

    game.p2_score_point()
    assert game.score() == "0:15"

    game.p2_score_point()
    assert game.score() == "0:30"

    game.p2_score_point()
    assert game.score() == "0:40"


def test_win_p2():
    game = Game()

    game.p2_score_point()
    game.p2_score_point()
    game.p2_score_point()
    game.p2_score_point()

    assert game.score() == "WIN P2"


def test_win_p1():
    game = Game()

    game.p1_score_point()
    game.p1_score_point()
    game.p1_score_point()
    game.p1_score_point()

    assert game.score() == "WIN P1"


def test_avantage():
    game = Game()

    game.p1_score_point()
    game.p1_score_point()
    game.p1_score_point()
    game.p2_score_point()
    game.p2_score_point()
    game.p2_score_point()

    game.p1_score_point()

    assert game.score() == "Ad:40"


def test_avantage_go_back():
    game = Game()

    game.p1_score_point()
    game.p1_score_point()
    game.p1_score_point()
    game.p2_score_point()
    game.p2_score_point()
    game.p2_score_point()
    game.p1_score_point()  # Ad:40

    game.p2_score_point()

    assert game.score() == "40:40"
