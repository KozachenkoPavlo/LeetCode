from typing import List


class Solution:
    # Time: O(N)
    # Space: O(1), don't count the result, since it is mandatory
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        keep = None

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                if keep is None:
                    keep = nums[i - 1]
            else:
                if keep is None:
                    result.append(str(nums[i - 1]))
                else:
                    result.append(f"{keep}->{nums[i - 1]}")
                    keep = None

        if keep is None:
            result.append(str(nums[-1]))
        else:
            result.append(f"{keep}->{nums[-1]}")

        return result
