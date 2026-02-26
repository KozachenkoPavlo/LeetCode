from typing import List

from math import inf


class Solution:
    def earliestFinishTime(
            self,
            landStartTime: List[int],
            landDuration: List[int],
            waterStartTime: List[int],
            waterDuration: List[int]
    ) -> int:
        result = inf

        def find_fastest(start_time_1: List[int], duration_1: List[int], start_time_2: List[int],
                         duration_2: List[int]) -> int:
            finish_1 = inf
            for st, d in zip(start_time_1, duration_1):
                finish_1 = min(finish_1, st + d)

            finish_2 = inf
            for st, d in zip(start_time_2, duration_2):
                finish_2 = min(finish_2, max(finish_1, st) + d)

            return finish_2

        return min(
            find_fastest(landStartTime, landDuration, waterStartTime, waterDuration),
            find_fastest(waterStartTime, waterDuration, landStartTime, landDuration),
        )
