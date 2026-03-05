from collections import Counter
from typing import List

from math import inf


class Solution:
    def get_most_frequent(self, collection: dict) -> int:
        m = -inf
        result = 0

        for key, value in collection.items():
            if m < value:
                m = value
                result = key

        del collection[result]

        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = [self.get_most_frequent(counter) for _ in range(k)]

        return result
