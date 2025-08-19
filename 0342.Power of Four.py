"""LeetCode 342: Power of Four — bitwise check"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Tagline: Bitwise power-of-four check.

        Intuition:
        A power of four is a power of two whose single set bit is in an even index.

        Approach:
        - Ensure n is positive.
        - Ensure only one bit is set (power of two) via n & (n - 1) == 0.
        - Ensure the set bit is in an even position by rejecting any set bit in odd positions using mask 0xAAAAAAAA.

        Complexity:
        Time: O(1)
        Space: O(1)
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0
