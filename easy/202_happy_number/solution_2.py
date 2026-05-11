class Solution:
    # Time: O(log N), don't really know why
    # Space: O(1)
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            result = 0

            while number:
                number, digit = divmod(number, 10)
                result += digit ** 2

            return result

        slow, fast = n, n

        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if slow == 1:
                return True

            if slow == fast:
                return False
