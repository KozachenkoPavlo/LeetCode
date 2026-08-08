from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        path = self

        for w in word:
            if w not in path.children:
                path.children[w] = TrieNode()
            path = path.children[w]

        path.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        height = len(board)
        width = len(board[0])
        visited = set()
        result = set()

        for word in words:
            root.insert(word)

        def dfs(row: int, col: int, node: TrieNode, word: str):
            if (0 > row or row >= height or 0 > col or col >= width or (row, col) in visited or board[row][
                col] not in node.children):
                return

            visited.add((row, col))

            if node.children[board[row][col]].is_word:
                result.add(word + board[row][col])

            dfs(row + 1, col, node.children[board[row][col]], word + board[row][col])
            dfs(row - 1, col, node.children[board[row][col]], word + board[row][col])
            dfs(row, col + 1, node.children[board[row][col]], word + board[row][col])
            dfs(row, col - 1, node.children[board[row][col]], word + board[row][col])

            visited.remove((row, col))

        for i in range(height):
            for j in range(width):
                dfs(i, j, root, "")

        return list(result)
