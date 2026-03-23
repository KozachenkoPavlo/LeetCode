from typing import List


class Solution:
    # Time: O(log(n * m)), where n is len(matrix[0]) and m is len(matrix)
    # Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, cols * rows - 1

        while l <= r:
            m = (l + r) // 2
            element = matrix[m // cols][m % cols]

            if element < target:
                l = m + 1
            elif element > target:
                r = m - 1
            else:
                return True

        return False
