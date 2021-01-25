class Database:
    def __init__(self):
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

    def count(self):
        return len(self.stuff)
