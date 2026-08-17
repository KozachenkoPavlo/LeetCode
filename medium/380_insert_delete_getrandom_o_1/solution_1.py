import random
from typing import List, Dict


class RandomizedSet:
    # Space: O(2 * N) -> O(N)
    def __init__(self):
        self.array: List[int] = list()
        self.registry: Dict[int, int] = dict()

    # Time: O(1)
    def insert(self, value) -> bool:
        if value in self.registry:
            return False

        self.registry[value] = len(self.array)
        self.array.append(value)

        return True

    # Time: O(1)
    def remove(self, value) -> bool:
        if value not in self.registry:
            return False

        index = self.registry[value]
        self.array[index] = self.array[-1]
        self.registry[self.array[-1]] = index

        self.array.pop()
        del self.registry[value]

        return True

    # Time: O(1)
    def getRandom(self) -> int:
        index = random.randint(0, len(self.array) - 1)
        return self.array[index]
