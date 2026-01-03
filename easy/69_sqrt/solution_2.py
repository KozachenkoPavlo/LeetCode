class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            cursor = (left + right) // 2

            if cursor * cursor == x:
                return cursor
            elif cursor * cursor > x:
                right = cursor - 1
            else:
                left = cursor + 1

        return right
