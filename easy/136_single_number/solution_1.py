from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        buffer = set()

        for num in nums:
            if num in buffer:
                buffer.remove(num)
            else:
                buffer.add(num)

        return buffer.pop()
