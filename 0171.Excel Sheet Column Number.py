class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """Base-26 conversion from column title to number.

        Intuition:
            Excel columns are essentially base-26 numbers where A=1, B=2, ...,
            Z=26. Process each character left to right, accumulating the result.

        Approach:
            1. Initialize result to 0.
            2. For each character, multiply current result by 26 and add the
               character's position (ord(c) - ord('A') + 1).

        Complexity:
            Time: O(n) where n is the length of columnTitle
            Space: O(1)
        """
        result = 0
        for char_code in map(ord, columnTitle):
            result = result * 26 + char_code - ord("A") + 1
        return result
