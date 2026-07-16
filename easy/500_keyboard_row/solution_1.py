from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]
        result = []

        for word in words:
            word_set = set(word.lower())

            for row in rows:
                if word_set.issubset(row):
                    result.append(word)

        return result
