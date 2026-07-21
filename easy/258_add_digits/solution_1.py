class Solution:
    def addDigits(self, num: int) -> int:
        result = 0

        while True:
            while 0 < num:
                result += num % 10
                num = num // 10

            if result < 10:
                return result
            else:
                num = result
                result = 0
