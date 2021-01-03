# En Java, en C++, les tests ressemblent plus à ça
#
# Notez également que si vous utilisez le module unittest
# plutôt que pytest, vous devrez obligatoirement utiliser
# des classes:
#   https://docs.python.org/3.8/library/unittest.html
#
# Exécutez avec pytest -v pour voir la différence

class TestSomething():
    def test_something_once(self):
        something = 0
        assert something == 0

    def test_something_twice(self):
        something = 12
        assert something > 0
        assert something is not None


class TestOtherStuff():
    def test_other_stuff(self):
        other_stuff = "hello, world"
        assert other_stuff.startswith("hello")
