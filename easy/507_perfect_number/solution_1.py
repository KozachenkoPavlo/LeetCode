class Solution:
    # Time: O(N ** O.5)
    # Space: O(1)
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        result = 1

        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                result += i

                if i != num // i:
                    result += num // i

        return result == num
