from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        registry = {}

        while strs:
            s = strs.pop()
            s_key = "".join(sorted(s))

            if s_key in registry:
                registry[s_key].append(s)
            else:
                registry[s_key] = [s]

        return list(registry.values())
