class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [c for c in s if c in set("aeiouAEIOU")]
        result = [vowels.pop() if c in set("aeiouAEIOU") else c for c in s]

        return "".join(result)
