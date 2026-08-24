from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        stack = []
        result = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == "1":
                    result += 1

                    grid[row][col] = "0"
                    stack.append((row, col))

                    while stack:
                        r, c = stack.pop()

                        if r > 0 and grid[r - 1][c] == "1":
                            grid[r - 1][c] = "0"
                            stack.append((r - 1, c))
                        if c > 0 and grid[r][c - 1] == "1":
                            grid[r][c - 1] = "0"
                            stack.append((r, c - 1))
                        if r + 1 < height and grid[r + 1][c] == "1":
                            grid[r + 1][c] = "0"
                            stack.append((r + 1, c))
                        if c + 1 < width and grid[r][c + 1] == "1":
                            grid[r][c + 1] = "0"
                            stack.append((r, c + 1))

        return result
