class Solution:
    def repeatedSubstringPattern(self, text: str) -> bool:
        """String doubling trick to detect repeated substring patterns.

        Intuition:
            If s is made of repeated substrings, then s appears in (s + s)
            at a position other than 0 and len(s). Equivalently, searching
            for s in (s + s) starting at index 1 should find it before index len(s).

        Approach:
            1. Concatenate the string with itself.
            2. Search for the original string starting from index 1.
            3. If found before index len(s), the string has a repeated pattern.

        Complexity:
            Time: O(n) using KMP or similar substring search.
            Space: O(n) for the doubled string.
        """
        return (text + text).index(text, 1) < len(text)
