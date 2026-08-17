import random
from typing import Set, List, Dict


class RandomizedCollection:
    # Space: O(2 * N) -> O(N)
    def __init__(self):
        self.array: List[int] = list()
        self.registry: Dict[int, Set] = dict()

    # Time: O(1)
    def insert(self, value) -> bool:
        result = False

        if value in self.registry:
            self.registry[value].add(len(self.array))
        else:
            result = True
            self.registry[value] = {len(self.array)}

        self.array.append(value)

        return result

    # Time: O(1)
    def remove(self, value) -> bool:
        if value not in self.registry:
            return False

        if len(self.array) == 1:
            self.array.pop()
            del self.registry[value]
            return True

        index = self.registry[value].pop()
        if not self.registry[value]:
            del self.registry[value]

        last_value = self.array[-1]
        if index != len(self.array) - 1:
            self.array[index] = self.array[-1]
            self.registry[last_value].remove(len(self.array) - 1)
            self.registry[last_value].add(index)

        self.array.pop()

        return True

    # Time: O(1)
    def getRandom(self) -> int:
        index = random.randint(0, len(self.array) - 1)
        return self.array[index]
