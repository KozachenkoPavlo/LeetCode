class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        result = ""

        while num != 0:
            print(f"Check {num}")
            num, left = divmod(num, 7)
            result = str(left) + result

        if negative:
            return "-" + result

        return result
