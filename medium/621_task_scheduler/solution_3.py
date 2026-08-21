from collections import Counter
from typing import List


class Solution:
    # Time: O(L + U) -> O(L)
    # Space: O(U) -> O(1)
    # Where:
    # L = len(tasks)
    # N = n
    # U = len(set(tasks))
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)  # O(L)
        max_frequency = max(counter.values())  # O(U)
        max_count = list(counter.values()).count(max_frequency)  # O(2 * U)
        max_length = (max_frequency - 1) * (n + 1) + max_count  # O(1)

        return max(len(tasks), max_length)
