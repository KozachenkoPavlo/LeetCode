import heapq

from typing import List


class Solution:
    # Time: O(N * log K)
    # Space: O(K)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x, y = point[0], point[1]
            distance = -(x ** 2 + y ** 2)

            if len(distances) < k:
                heapq.heappush(distances, (distance, x, y))
            else:
                heapq.heappushpop(distances, (distance, x, y))

        return [[x, y] for _, x, y in distances]
