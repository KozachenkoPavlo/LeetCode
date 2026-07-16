from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        result = []

        for word in words:
            row = ""

            for index in range(len(rows)):
                if word[0].lower() in rows[index]:
                    row = rows[index]

            for char in word:
                if char.lower() not in row:
                    break
            else:
                result.append(word)

        return result
