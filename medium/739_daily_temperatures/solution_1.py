from typing import List


class Solution:
    # Time: O(2*n) -> O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                previous_temperature = stack.pop()
                result[previous_temperature] = i - previous_temperature

            stack.append(i)

        return result
