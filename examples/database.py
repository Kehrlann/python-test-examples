from time import sleep

class Database:
    def __init__(self):
        sleep(0)
        self.stuff = {}

    def cleanup(self):
        self.stuff = {}

    def save(self, id, timestamp, count):
        self.stuff[id] = {
            'timestamp': timestamp,
            'count': count
        }

    def find_all(self, id):
        return [self.stuff[id]]

    def remove(self, id):
        self.stuff.pop(id, None)

    def count(self):
        return len(self.stuff)
