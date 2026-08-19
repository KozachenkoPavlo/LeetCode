import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = string.ascii_lowercase + string.digits

        result = []
        for i in s:
            i = i.lower()
            if i in allowed:
                result.append(i)

        return result == result[::-1]
