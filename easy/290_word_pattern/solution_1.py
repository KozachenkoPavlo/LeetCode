class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        registry = {}
        seen_words = set()
        words = s.split()

        if len(words) != len(pattern):
            return False

        for c, word in zip(pattern, words):
            if c in registry.keys():
                if registry[c] != word:
                    return False
            else:
                if word in seen_words:
                    return False

                registry[c] = word
                seen_words.add(word)

        return True
