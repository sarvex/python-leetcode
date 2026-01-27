class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """Check if capital usage in a word follows valid patterns.

        Intuition:
            Valid patterns are: all uppercase, all lowercase, or only the
            first letter uppercase. Count uppercase letters to determine.

        Approach:
            Count uppercase characters. Return True if count is 0 (all lower),
            equals length (all upper), or is 1 with first letter uppercase.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        upper_count = sum(char.isupper() for char in word)
        return (
            upper_count == 0
            or upper_count == len(word)
            or (upper_count == 1 and word[0].isupper())
        )
