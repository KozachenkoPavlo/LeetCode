from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        last = timeSeries[0]

        for t in timeSeries[1:]:
            result += min(duration, t - last)
            last = t

        return result + duration
