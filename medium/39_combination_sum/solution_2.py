from typing import List


class Solution:
    # Time: O(N ** (target / min(nums))
    # Formula: (Max amount of branches) ** (Max depth of the recursion)
    # Space: O(target / min(nums))
    # Max depth of the tree is our Space complexity (We don't count result as it is required by the problem).
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        temp_nums = []
        temp_sum = 0

        nums.sort()

        def backtrace(pointer: int = 0):
            nonlocal temp_sum

            if temp_sum == target:
                result.append(temp_nums.copy())
                return

            for index in range(pointer, len(nums)):
                num = nums[index]

                if temp_sum + num > target:
                    break  # We can do it because the list is sorted

                temp_nums.append(num)
                temp_sum += num

                backtrace(index)

                temp_nums.pop()
                temp_sum -= num

        backtrace()

        return result
