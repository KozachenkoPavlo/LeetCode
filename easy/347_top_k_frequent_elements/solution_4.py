from collections import Counter
from typing import List


class Solution:
    # O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums))]

        for value, freq in count.items():
            buckets[freq - 1].append(value)

        for bucket in reversed(buckets):
            if len(result) < k:
                result.extend(bucket)

        return result[:k]
