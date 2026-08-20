import heapq
from collections import Counter
from typing import List


class Solution:
    # Time: O(L * N * U) -> O(L * N)
    # Space: O(U) -> O(1)
    # Where:
    # L = len(tasks)
    # N = n
    # U = len(set(tasks))
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-value, key) for key, value in Counter(tasks).items()]  # O(L)
        heapq.heapify(heap)  # O(U)

        cpu_cycle = 0
        processed = []

        while heap or processed:  # O(L * N)
            cpu_cycle += 1

            while processed and cpu_cycle - processed[0][0] > n:  # O(U)
                _, value, task = heapq.heappop(processed)  # O(log U)
                heapq.heappush(heap, (value, task))  # O(log U)

            if heap:
                value, task = heapq.heappop(heap)  # O(log U)

                if -value > 1:
                    heapq.heappush(processed, (cpu_cycle, value + 1, task))  # O(log U)

        return cpu_cycle


if __name__ == "__main__":
    s = Solution()
    result = s.leastInterval(["A", "A", "A", "B", "C"], 3)
    print(result)

    result = s.leastInterval(["X", "X", "Y", "Y"], 2)
    print(result)
