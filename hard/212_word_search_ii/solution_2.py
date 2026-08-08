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

    def remove(self, word: str, index: int = 0) -> bool:
        if index == len(word):
            self.word = None
            return len(self.children) == 0

        char = word[index]
        if char not in self.children:
            return False

        child = self.children[char]
        can_delete_child = child.remove(word, index + 1)

        if can_delete_child:
            del self.children[char]
            return self.word is None and len(self.children) == 0

        return False


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
                root.remove(word)

            dfs(row + 1, col, node.children[key])
            dfs(row - 1, col, node.children[key])
            dfs(row, col + 1, node.children[key])
            dfs(row, col - 1, node.children[key])

            board[row][col] = key

        for i in range(height):
            for j in range(width):
                dfs(i, j, root)

        return list(result)
