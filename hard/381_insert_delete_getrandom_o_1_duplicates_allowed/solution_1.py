import random
from collections import defaultdict
from typing import Set, List, Dict


class RandomizedCollection:
    # Space: O(2 * N) -> O(N)
    def __init__(self):
        self.array: List[int] = list()
        self.registry: Dict[int, Set] = defaultdict(set)

    # Time: O(1)
    def insert(self, value) -> bool:
        self.registry[value].add(len(self.array))
        self.array.append(value)

        return len(self.registry[value]) == 1

    # Time: O(1)
    def remove(self, value) -> bool:
        if value not in self.registry:
            return False

        remove_index, last_value = self.registry[value].pop(), self.array[-1]

        self.array[remove_index] = last_value
        self.registry[last_value].add(remove_index)
        self.registry[last_value].discard(len(self.array) - 1)

        if not self.registry[value]:
            del self.registry[value]

        self.array.pop()

        return True

    # Time: O(1)
    def getRandom(self) -> int:
        if self.array:
            return random.choice(self.array)

        return -1
