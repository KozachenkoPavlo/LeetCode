from collections import defaultdict
from typing import List


class Solution:
    """
    O(N * K)
    N : len(strs)
    K : len(strs[index])
    """
    def get_key(self, s: str) -> tuple:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        registry = defaultdict(list)

        for s in strs:
            key = self.get_key(s)

            registry[key].append(s)

        return list(registry.values())
