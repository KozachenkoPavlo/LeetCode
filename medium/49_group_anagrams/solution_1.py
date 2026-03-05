from collections import Counter
from typing import List


class Solution:
    # Too slow
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        def is_anagram(s1: str, s2: str) -> bool:
            return Counter(s1) == Counter(s2)

        while strs:
            s = strs.pop()
            result.append([s])

            for i in range(len(strs) - 1, -1, -1):
                if is_anagram(s, strs[i]):
                    result[-1].append(strs.pop(i))

        return result
