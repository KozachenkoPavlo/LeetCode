import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x, y = point[0], point[1]
            distance = ((x ** 2 + y ** 2) ** 2) ** 0.5
            heapq.heappush(distances, (distance, x, y))

        return [[x, y] for _, x, y in heapq.nsmallest(k, distances)]
