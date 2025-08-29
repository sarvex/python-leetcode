class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Bit manipulation approach to check if integer is a power of two.

        Intuition:
            Powers of two in binary have exactly one bit set (e.g., 1, 10, 100, 1000).
            For any power of two n, n-1 flips all bits after the single set bit.
            Therefore, n & (n-1) will be 0 if n is a power of two.

        Approach:
            1. First check if n > 0 (powers of two are positive)
            2. Then apply bit manipulation trick: n & (n-1) == 0

        Complexity:
            - Time: O(1), constant time bit operations
            - Space: O(1), no additional space needed

        Args:
            n: Integer to check

        Returns:
            True if n is a power of two, False otherwise

        Examples:
            >>> Solution().isPowerOfTwo(1)
            True
            >>> Solution().isPowerOfTwo(16)
            True
            >>> Solution().isPowerOfTwo(3)
            False
        """
        # Powers of two must be positive integers
        # For powers of two, n & (n-1) equals 0 due to bit manipulation properties
        return n > 0 and (n & (n - 1)) == 0
