from typing import List

import math


class Solution:
    def earliestFinishTime(
            self,
            landStartTime: List[int],
            landDuration: List[int],
            waterStartTime: List[int],
            waterDuration: List[int]
    ) -> int:
        result = math.inf

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                result = min(result, max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j])
                result = min(result, max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i])

        return result
