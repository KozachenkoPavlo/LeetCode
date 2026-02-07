from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        log = {}

        for n in nums1:
            if n not in log.keys():
                log[n] = 1
            else:
                log[n] += 1

        result = []

        for n in nums2:
            if n in log.keys():
                result.append(n)

                if log[n] == 1:
                    del log[n]
                else:
                    log[n] -= 1

        return result
