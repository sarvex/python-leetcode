class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """Bit manipulation using XOR and popcount.

        Intuition:
            XOR of two numbers produces a number with 1-bits exactly where
            the two numbers differ.

        Approach:
            XOR x and y, then count the number of set bits in the result.

        Complexity:
            Time: O(1) — fixed 32-bit integers
            Space: O(1)
        """
        return (x ^ y).bit_count()
