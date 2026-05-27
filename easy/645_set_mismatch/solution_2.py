from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        lost = -1

        for num in nums:
            value = abs(num)
            index = value - 1

            if nums[index] < 0:
                duplicate = value
            else:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                lost = i + 1
            else:
                nums[i] = -nums[i]

        return [duplicate, lost]
