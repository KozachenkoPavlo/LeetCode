from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for key in t_counter.keys():
            if key not in s_counter.keys() or s_counter[key] < t_counter[key]:
                return key

        return ""
