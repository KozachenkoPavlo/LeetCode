from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        registry = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            registry[key].append(s)

        return list(registry.values())
