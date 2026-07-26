class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = []
        p1 = len(num1) - 1
        p2 = len(num2) - 1

        while p1 >= 0 or p2 >= 0 or carry != 0:
            n1 = int(num1[p1]) if p1 >= 0 else 0
            n2 = int(num2[p2]) if p2 >= 0 else 0

            carry, r = divmod(n1 + n2 + carry, 10)

            result.append(str(r))
            p1 -= 1
            p2 -= 1

        return "".join(reversed(result))
