from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word: str) -> None:
        path = self

        for w in word:
            if w not in path.children:
                path.children[w] = TrieNode()
            path = path.children[w]

        path.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        height = len(board)
        width = len(board[0])
        result = set()

        for word in words:
            root.insert(word)

        def dfs(row: int, col: int, node: TrieNode):
            if 0 > row or row >= height or 0 > col or col >= width or board[row][col] not in node.children:
                return

            key = board[row][col]
            board[row][col] = "*"

            if word := node.children[key].word:
                result.add(word)

            dfs(row + 1, col, node.children[key])
            dfs(row - 1, col, node.children[key])
            dfs(row, col + 1, node.children[key])
            dfs(row, col - 1, node.children[key])

            board[row][col] = key

        for i in range(height):
            for j in range(width):
                dfs(i, j, root)

        return list(result)
