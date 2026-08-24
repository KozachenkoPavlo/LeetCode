import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    # Time: O(log(N / 2)) -> O(log N)
    def addNum(self, num: int) -> None:
        if self.min_heap and num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) - 1 > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.min_heap) - 1 > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    # Time: O(1)
    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2

        if len(self.min_heap) < len(self.max_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])
