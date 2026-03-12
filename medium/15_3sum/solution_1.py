from typing import List


class Solution:
    # Time: O(n**2)
    # Space: O(n), because we have additional set
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n * lon(n))
        result = set()

        # O(n**2)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    triple_tuple = (nums[i], nums[l], nums[r])
                    if triple_tuple not in result:
                        result.add(triple_tuple)
                    l += 1

        return [list(t) for t in result]
