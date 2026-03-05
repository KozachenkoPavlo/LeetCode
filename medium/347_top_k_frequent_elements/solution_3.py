import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        for num, freq in count.items():
            heapq.heappush(result, (freq, num))

            if len(result) > k:
                heapq.heappop(result)

        return [i for _, i in result]
