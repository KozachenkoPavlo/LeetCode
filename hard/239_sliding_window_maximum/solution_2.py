from collections import deque
from typing import List


class DecreasingMonotonicStack:
    def __init__(self, init_list: list[int] | None = None):
        self.stack = deque()

        if init_list is None:
            return

        for element in init_list:
            self.add(element)

    def add(self, element: int):
        while self.stack and self.stack[-1] < element:
            self.stack.pop()

        self.stack.append(element)

    def remove(self, element: int):
        if self.stack[0] == element:
            self.stack.popleft()

    def get_biggest(self):
        return self.stack[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p1, p2 = 0, k
        result = []
        deque = DecreasingMonotonicStack(nums[p1:p2])

        while True:
            result.append(deque.get_biggest())

            if p2 >= len(nums):
                break

            deque.remove(nums[p1])
            deque.add(nums[p2])

            p1 += 1
            p2 += 1

        return result


if __name__ == "__main__":
    s = Solution()
    tests = [
        {"args": ([1, 2, 1, 0, 4, 2, 6], 3), "result": [2, 2, 4, 4, 6]},
        {"args": ([1], 1), "result": [1]}
    ]

    for test in tests:
        result = s.maxSlidingWindow(*test["args"])

        if result == test["result"]:
            print("PASSED!")
        else:
            print(f"Result: {result}")
            print(f"Expected: {test['result']}")
