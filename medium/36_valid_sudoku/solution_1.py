from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)

        # Check horizontal
        for line in board:
            registry = set()

            for num in line:
                if num != ".":
                    if num in registry:
                        return False
                    else:
                        registry.add(num)

        # Check vertical
        for col in range(size):
            registry = set()

            for row in range(size):
                num = board[row][col]

                if num != ".":
                    if num in registry:
                        return False
                    else:
                        registry.add(num)

        # Check block
        for col in range(1, size, 3):
            for row in range(1, size, 3):
                registry = set()

                for c in range(col - 1, col + 2):
                    for r in range(row - 1, row + 2):
                        num = board[c][r]

                        if num != ".":
                            if num in registry:
                                return False
                            else:
                                registry.add(num)

        return True
