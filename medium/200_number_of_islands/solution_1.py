from typing import List


# Time: O(N * M)
# Space: O(N * M)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        taken = set()
        height = len(grid)
        width = len(grid[0])
        result = 0

        def register_island(row: int, col: int):
            if (row < 0
                    or col < 0
                    or row >= height
                    or col >= width
                    or grid[row][col] == "0"
                    or (row, col) in taken):
                return

            taken.add((row, col))
            register_island(row, col + 1)
            register_island(row + 1, col)
            register_island(row, col - 1)
            register_island(row - 1, col)

        for row in range(height):
            for col in range(width):
                if (row, col) not in taken and grid[row][col] == "1":
                    result += 1
                    register_island(row, col)

        return result
