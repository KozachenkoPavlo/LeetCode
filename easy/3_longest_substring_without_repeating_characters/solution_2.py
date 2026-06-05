class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        registry = set()
        slow_pointer = 0
        max_length = 0

        for fast_pointer in range(len(s)):
            while s[fast_pointer] in registry:
                registry.remove(s[slow_pointer])
                slow_pointer += 1

            registry.add(s[fast_pointer])

            current_window_size = fast_pointer - slow_pointer + 1
            max_length = max(max_length, current_window_size)

        return max_length
