class Solution:
    # Time: O(N)
    # Space: O(1)
    def detectCapitalUse(self, word: str) -> bool:
        all_capital = True
        all_small = True
        capitalized = True

        for i in range(len(word)):
            if all_small and word[i].isupper():
                all_small = False
            if all_capital and word[i].islower():
                all_capital = False
            if capitalized and ((i == 0 and word[i].islower()) or (i != 0 and word[i].isupper())):
                capitalized = False

        return all_capital or all_small or capitalized
