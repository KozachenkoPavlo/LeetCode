class Solution:
    # Time: O(N)
    # Space: O(1), because 's' contains only alphabetical characters
    def characterReplacement(self, s: str, k: int) -> int:
        registry = {}
        max_frequent = 0
        fast, slow = 0, 0

        for fast in range(len(s)):
            registry[s[fast]] = registry.get(s[fast], 0) + 1
            max_frequent = max(max_frequent, registry[s[fast]])

            if (fast - slow + 1) - max_frequent > k:
                registry[s[slow]] -= 1
                slow += 1

        return fast - slow + 1
