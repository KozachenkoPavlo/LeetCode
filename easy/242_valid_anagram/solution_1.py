class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def register_word(word: str) -> dict:
            d = {}

            for c in word:
                if c in d.keys():
                    d[c] += 1
                else:
                    d[c] = 1

            return d

        return register_word(s) == register_word(t)
