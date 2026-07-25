class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        roll_over = False
        result = []

        for i in range(max(len(num1), len(num2))):
            if i >= len(num1):
                n1 = 0
            else:
                n1 = int(num1[-1 - i])

            if i >= len(num2):
                n2 = 0
            else:
                n2 = int(num2[-1 - i])

            r = n1 + n2

            if roll_over:
                r += 1
                roll_over = False

            if r > 9:
                r %= 10
                roll_over = True

            result.append(str(r))

        if roll_over:
            result.append("1")

        return "".join(reversed(result))