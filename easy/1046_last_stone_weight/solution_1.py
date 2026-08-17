import heapq
from typing import List


class Solution:
    # Time: O(N * log N). Loop( O(N) ) * Heappop & Heappush( log N )
    # Space: O(N). Heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone_1 = heapq.heappop(heap)
            stone_2 = heapq.heappop(heap)

            if stone_1 == stone_2:
                continue

            heapq.heappush(heap, stone_1 - stone_2)

        return -heapq.heappop(heap) if heap else 0
