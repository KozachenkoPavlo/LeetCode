from collections import Counter


class Solution:
    # Time: O(1), because len(s1) == len(s2) == 4
    # Space: O(1)
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])