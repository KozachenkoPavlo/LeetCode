class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        if num < 0:
            num = 16 ** 8 + num

        while num:
            n = num & 15
            result.append(hex_chars[n])
            num >>= 4

        return "".join(result[::-1])
