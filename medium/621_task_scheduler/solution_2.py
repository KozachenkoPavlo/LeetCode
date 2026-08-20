import heapq
from collections import Counter, deque
from typing import List


class Solution:
    # Time: O(L * U) -> O(L)
    # Space: O(U) -> O(1)
    # Where:
    # L = len(tasks)
    # N = n
    # U = len(set(tasks))
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-value, key) for key, value in Counter(tasks).items()]  # O(L)
        heapq.heapify(heap)  # O(U)

        cpu_cycle = 0
        processed = deque()

        while heap or processed:  # O(L)
            if not heap and cpu_cycle - processed[0][0] <= n:
                cpu_cycle = processed[0][0] + n

            cpu_cycle += 1

            while processed and cpu_cycle - processed[0][0] > n:  # O(U)
                _, value, task = processed.popleft()  # O(1)
                heapq.heappush(heap, (value, task))  # O(log U)

            if heap:
                value, task = heapq.heappop(heap)  # O(log U)

                if -value > 1:
                    processed.append((cpu_cycle, value + 1, task))  # O(1)

        return cpu_cycle


if __name__ == "__main__":
    s = Solution()
    result = s.leastInterval(["A", "A", "A", "B", "C"], 3)
    print(result)

    result = s.leastInterval(["X", "X", "Y", "Y"], 2)
    print(result)
