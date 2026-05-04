class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stored = 0
        self.cache = {}
        self.priority = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.prioritize_key(key)

            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            self.cache[key] = value

            if self.capacity > self.stored:
                self.stored += 1
            else:
                self.remove_last()

        self.prioritize_key(key)

    def prioritize_key(self, key: int):
        if key in self.priority:
            self.priority.remove(key)

        self.priority.insert(0, key)

    def remove_last(self):
        del self.cache[self.priority[-1]]
        del self.priority[-1]
