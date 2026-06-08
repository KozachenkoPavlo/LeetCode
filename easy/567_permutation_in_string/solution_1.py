from collections import Counter


class Solution:
    def is_permutable(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        for p1, p2 in [(i, i + len(s1)) for i in range(len(s2))]:
            if self.is_permutable(s1, s2[p1:p2]):
                return True

        return False
