from examples.database import Database
from datetime import datetime


class TestSetupClass():
    """
    Class setup and teardown:
    - UNE FOIS par classe
    - Utilisable dans toutes les méthodes de test
    - Un changement dans un test impacte tous les autres ("pollution")

    Pour des opérations "coûteuses" (par exemple: lentes)
    """
    @classmethod
    def setup_class(cls):
        cls.db = Database()

    def setup_method(self):
        self.db.cleanup()

    @classmethod
    def teardown_class(cls):
        cls.db.cleanup()

    def test_save_one_record(self):
        ts = datetime.now()
        self.db.save('1X00021', ts,  5)

        assert self.db.count() == 1
        assert self.db.find_all("1X00021") == [{"timestamp": ts, "count": 5}]

    def test_save_multiple_records(self):
        self.db.save('1XB2344', datetime.now(),  5)
        self.db.save('2Y080A1', datetime.now(),  -1)

        assert self.db.count() == 2

    def test_save_same_record_twice(self):
        self.db.save('0X00000', datetime.now(),  5)
        self.db.save('0X00000', datetime.now(),  -1)

        assert len(self.db.find_all('0X00000')) == 1
