from collections import deque
from typing import List


class Solution:
    # Time: O((N * M) ** 2)
    # Space: O(N * M)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])

        def dfs(r: int, c: int) -> bool:
            nonlocal height, width
            is_pacific = False
            is_atlantic = False
            queue = deque([(r, c)])
            seen = {(r, c)}

            while queue:
                row, col = queue.popleft()

                if row == 0 or col == 0:
                    is_pacific = True
                if row == height - 1 or col == width - 1:
                    is_atlantic = True

                if is_pacific and is_atlantic:
                    return True

                current_height = heights[row][col]

                if col + 1 < width and current_height >= heights[row][col + 1] and (row, col + 1) not in seen:
                    seen.add((row, col + 1))
                    queue.append((row, col + 1))
                if row + 1 < height and current_height >= heights[row + 1][col] and (row + 1, col) not in seen:
                    seen.add((row + 1, col))
                    queue.append((row + 1, col))
                if col > 0 and current_height >= heights[row][col - 1] and (row, col - 1) not in seen:
                    seen.add((row, col - 1))
                    queue.append((row, col - 1))
                if row > 0 and current_height >= heights[row - 1][col] and (row - 1, col) not in seen:
                    seen.add((row - 1, col))
                    queue.append((row - 1, col))

            return False

        result = []

        for row in range(height):
            for col in range(width):
                if dfs(row, col):
                    result.append([row, col])

        return result
