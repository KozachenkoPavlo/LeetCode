import heapq
from typing import List


class Solution:
    # Time: O(N * log K)
    # Space: O(K)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heap[0]
