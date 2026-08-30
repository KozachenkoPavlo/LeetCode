class Solution:
    # Time: O(N)
    # Space: O(1), even though we have a list, it is constant because of a number constraint
    def largestString(self, nums: list[int]) -> list[str]:
        result = []

        for num in nums:
            r = ["z" * (num // 2 ** 25)]
            bits = f"{num:025b}"[-25:]

            for i, b in enumerate(bits):
                if b == "1":
                    r.append(chr(121 - i))

            result.append("".join(r))

        return result