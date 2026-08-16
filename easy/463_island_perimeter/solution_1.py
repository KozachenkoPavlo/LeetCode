from typing import List


class Solution:
    # Time: O(N * M), where N is a width, and M is a height
    # Space: O(N * M), because of recursion in case the whole grid has only 1
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        def backtrace(row: int, col: int):
            if row < 0 or row >= height or col < 0 or col >= width or grid[row][col] == 0:
                return 1

            if grid[row][col] == -1:
                return 0

            grid[row][col] = -1

            return (
                    backtrace(row, col + 1)
                    + backtrace(row + 1, col)
                    + backtrace(row, col - 1)
                    + backtrace(row - 1, col)
            )

        for r in range(height):
            for c in range(width):
                if grid[r][c]:
                    return backtrace(r, c)

        return 0