from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = Counter(s1)

        for p1, p2 in [(i, i + len(s1)) for i in range(len(s2))]:
            if s1_hash == Counter(s2[p1:p2]):
                return True

        return False
