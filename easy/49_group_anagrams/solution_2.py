from collections import Counter
from typing import List


class Solution:
    def is_anagram(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

    # Too slow
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        s = strs.pop()
        registry = {
            len(s): [[s]],
        }

        while strs:
            s = strs.pop()

            if len(s) not in registry:
                registry[len(s)] = [[s]]
                continue

            for i in range(len(registry[len(s)])):
                if self.is_anagram(registry[len(s)][i][0], s):
                    registry[len(s)][i].append(s)
                    break
            else:
                registry[len(s)].append([s])

        result = []

        for value in registry.values():
            for v in value:
                result.append(v)

        return result
