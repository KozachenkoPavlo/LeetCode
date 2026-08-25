from typing import List


class Solution:
    # Time: O(N * M)
    # Space: O(N * M)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        result = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    stack = [(row, col)]
                    grid[row][col] = 0
                    current = 1

                    while stack:
                        r, c = stack.pop()

                        if r > 0 and grid[r - 1][c] == 1:
                            grid[r - 1][c] = 0
                            current += 1
                            stack.append((r - 1, c))
                        if r + 1 < height and grid[r + 1][c] == 1:
                            grid[r + 1][c] = 0
                            current += 1
                            stack.append((r + 1, c))
                        if c > 0 and grid[r][c - 1] == 1:
                            grid[r][c - 1] = 0
                            current += 1
                            stack.append((r, c - 1))
                        if c + 1 < width and grid[r][c + 1] == 1:
                            grid[r][c + 1] = 0
                            current += 1
                            stack.append((r, c + 1))

                    result = max(current, result)

        return result
