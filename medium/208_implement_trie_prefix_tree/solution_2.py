class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        path = self.root

        for w in word:
            if w not in path:
                path[w] = {}
            path = path[w]

        path[None] = None

    def search(self, word: str) -> bool:
        path = self.root

        for w in word:
            if w not in path:
                return False

            path = path[w]

        return None in path

    def startsWith(self, prefix: str) -> bool:
        path = self.root

        for w in prefix:
            if w not in path:
                return False

            path = path[w]

        return True
