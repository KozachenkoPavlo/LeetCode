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

        for l_st, l_d in zip(landStartTime, landDuration):
            for w_st, w_d in zip(waterStartTime, waterDuration):
                land_water = max(l_st + l_d, w_st) + w_d
                water_land = max(w_st + w_d, l_st) + l_d

                result = min(result, land_water, water_land)

        return result
