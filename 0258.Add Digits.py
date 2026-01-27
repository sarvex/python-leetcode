class Solution:
    def addDigits(self, num: int) -> int:
        """Digital root using the mathematical congruence formula.

        Intuition:
            The digital root of a number follows a pattern based on modulo 9
            arithmetic, allowing an O(1) solution without repeated digit summing.

        Approach:
            1. If num is 0, return 0 directly.
            2. Otherwise, use the formula (num - 1) % 9 + 1 to compute
               the digital root in constant time.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return 0 if num == 0 else (num - 1) % 9 + 1
