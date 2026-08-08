class WordDictionary:

    def __init__(self):
        self.registry = dict()

    def addWord(self, word: str) -> None:
        pointer = self.registry

        for w in word:
            if w not in pointer:
                pointer[w] = {}

            pointer = pointer[w]

        pointer[None] = None

    def search(self, word: str, pointer: dict | None = None) -> bool:
        if pointer is None:
            pointer = self.registry

        for i, w in enumerate(word):
            if w == ".":
                for key in pointer.keys():
                    if key is not None and self.search(word[i + 1:], pointer[key]):
                        return True
                return False

            if w not in pointer:
                return False

            pointer = pointer[w]

        return None in pointer

