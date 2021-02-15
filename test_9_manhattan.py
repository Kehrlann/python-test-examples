from examples.manhattan import manhattan


def test_same_point():
    assert manhattan((3, 1), (3, 1)) == 0


def test_down():
    assert manhattan((3, 1), (3, 3)) == 2


def test_up():
    assert manhattan((0, 3), (0, 0)) == 3


def test_right():
    assert manhattan((4, 6), (8, 6)) == 4


def test_left():
    assert manhattan((8, 6), (4, 6)) == 4


def test_nominal():
    assert manhattan((0, 0), (4, 4)) == 8
