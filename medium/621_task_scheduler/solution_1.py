import heapq
from collections import Counter
from typing import List


class Solution:
    # Do not pass by Time Limit
    # Time: O(L * N * U * log U)
    # Space: O(U)
    # Where:
    # L = len(tasks)
    # N = n
    # U = len(set(tasks))
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-value, key) for key, value in Counter(tasks).items()]  # O(L)
        heapq.heapify(heap)  # O(U)

        cpu_cycle = 0
        process_log = {}

        while heap:  # O(L * N - L + 1)
            buffer = []

            while heap:  # O(U)
                count, task = heapq.heappop(heap)
                count = -count

                if task not in process_log or cpu_cycle - process_log.get(task) > n:  # O(1)
                    process_log[task] = cpu_cycle  # O(1)

                    if count > 1:
                        heapq.heappush(heap, (-count + 1, task))  # O(log U)

                    break
                else:
                    heapq.heappush(buffer, (-count, task))  # O(log U)
                    continue

            cpu_cycle += 1

            while buffer:  # O(U)
                heapq.heappush(heap, heapq.heappop(buffer))  # O(log U)

        return cpu_cycle


if __name__ == "__main__":
    s = Solution()
    result = s.leastInterval(["A", "A", "A", "B", "C"], 3)
    print(result)

    result = s.leastInterval(["X", "X", "Y", "Y"], 2)
    print(result)
