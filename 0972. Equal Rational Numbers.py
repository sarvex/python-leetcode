from math import floor


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        """Expand repeating decimals and compare rounded numeric values.

        Intuition:
        Rational numbers with repeating decimals can be compared by expanding
        the repeating part sufficiently and rounding to enough decimal places
        to eliminate representation differences.

        Approach:
        1. Expand repeating part (in parentheses) by appending it multiple times
        2. Convert both strings to floating-point numbers
        3. Round to 8 decimal places and compare

        Complexity:
        Time: O(n) where n is the string length
        Space: O(n) for the expanded string
        """

        def expand_repeating(string: str) -> str:
            if "(" in string:
                repeating_part = string[string.index("(") + 1 : string.index(")")]
                string = string.replace("(", "").replace(")", "")
                string += repeating_part * 8
            return string

        def round_down(num: str, decimals: int) -> float:
            return floor(float(num) * 10**decimals + 0.5) / 10**decimals

        return round_down(expand_repeating(s), 8) == round_down(expand_repeating(t), 8)
