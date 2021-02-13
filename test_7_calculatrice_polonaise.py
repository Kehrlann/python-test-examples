from examples import rpn


def test_nothing():
    assert rpn.compute("") == 0


def test_one_number():
    assert rpn.compute("1") == 1


def test_add():
    assert rpn.compute("1 2 +") == 3


def test_two_adds():
    assert rpn.compute("1 2 3 + +") == 6


def test_subtract():
    assert rpn.compute("1 2 -") == -1


def test_multiply():
    assert rpn.compute("3 2 *") == 6


def test_divide():
    assert rpn.compute("4 2 /") == 2
