class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        registry = set()

        slow_pointer, fast_pointer = 0, 0
        length = len(s)

        while fast_pointer < length:
            fast_value = s[fast_pointer]

            if fast_value in registry:
                result = max(result, fast_pointer - slow_pointer)

                while slow_pointer < fast_pointer:
                    if s[slow_pointer] == fast_value:
                        slow_pointer += 1
                        break
                    else:
                        registry.remove(s[slow_pointer])
                        slow_pointer += 1
            else:
                registry.add(fast_value)

            fast_pointer += 1

        if result == 0 and length != 0:
            return length

        return max(result, fast_pointer - slow_pointer)
