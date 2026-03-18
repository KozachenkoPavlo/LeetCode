from typing import List


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(list(zip(position, speed)), reverse=True)
        stack = []

        for fleet in fleets:
            time = (target - fleet[0]) / fleet[1]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
