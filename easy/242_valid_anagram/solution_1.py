class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def register_word(word: str) -> dict:
            d = {}

            for c in word:
                d[c] = d.get(c, 0) + 1

            return d

        return register_word(s) == register_word(t)
