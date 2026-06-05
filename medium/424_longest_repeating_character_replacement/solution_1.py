class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        registry = {}
        slow = 0

        for fast in range(len(s)):
            registry[s[fast]] = registry.get(s[fast], 0) + 1

            while (fast - slow + 1) - max(registry.values()) > k:
                registry[s[slow]] -= 1
                slow += 1

            result = max(result, fast - slow + 1)

        return result
