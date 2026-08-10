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

        def backtrace(pointer: int = 0) -> bool:
            nonlocal temp_sum

            if temp_sum > target:
                return False

            if temp_sum == target:
                result.append(temp_nums.copy())
                return False

            for index in range(pointer, len(nums)):
                num = nums[index]
                temp_nums.append(num)
                temp_sum += num

                to_continue = backtrace(index)

                temp_nums.pop()
                temp_sum -= num

                if not to_continue:
                    break

            return True

        backtrace()

        return result
