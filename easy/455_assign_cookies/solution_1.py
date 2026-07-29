from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        child, bag = len(g) - 1, len(s) - 1
        g.sort()
        s.sort()

        while child >= 0 and bag >= 0:
            if g[child] <= s[bag]:
                result += 1
                bag -= 1

            child -= 1

        return result
