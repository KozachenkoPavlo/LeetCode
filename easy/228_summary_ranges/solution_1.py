from math import inf
from typing import List


class Solution:
    # Time: O(N)
    # Space: O(1), don't count the result, since it is mandatory
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        nums.append(inf)

        previous = nums[0]
        result = [str(previous)]
        length = 1

        for num in nums[1:]:
            if previous + 1 == num:
                length += 1
            else:
                if length > 1:
                    result[-1] += f'->{previous}'

                result.append(str(num))

                length = 1

            previous = num

        if result[-1] == "inf":
            result.pop()

        return result
