from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash = dict(Counter(s1))
        s2_hash = dict(Counter(s2[0:len(s1)]))
        p1, p2 = 0, len(s1)

        while True:
            if s1_hash == s2_hash:
                return True

            if p2 >= len(s2):
                break

            s2_hash[s2[p1]] -= 1
            if s2_hash[s2[p1]] == 0:
                del s2_hash[s2[p1]]

            s2_hash[s2[p2]] = s2_hash.get(s2[p2], 0) + 1

            p1 += 1
            p2 += 1

        return False
