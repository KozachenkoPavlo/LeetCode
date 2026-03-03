import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = [(value, key) for key, value in count.items()]

        return [i for _, i in heapq.nlargest(k, result)]
