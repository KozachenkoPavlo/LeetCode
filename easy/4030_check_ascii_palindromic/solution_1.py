class Solution:
    def isPalindromic(self, s: str) -> bool:
        sb = []

        for letter in s:
            sb.append(bin(ord(letter))[2:].zfill(8))

        sb = "".join(sb)
        l, r = 0, len(sb) - 1

        while l < r:
            if sb[l] != sb[r]:
                return False

            l += 1
            r -= 1

        return True
