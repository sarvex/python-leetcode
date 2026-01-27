class Solution:
    def queryString(self, s: str, n: int) -> bool:
        """Check if binary representations of 1 to n are all substrings of s.

        Intuition:
            For large n the string cannot contain enough distinct substrings.
            For smaller n, check from n downward since larger numbers are harder
            to find and we can short-circuit early.

        Approach:
            If n > 1000, return False immediately (pigeonhole on string length).
            Otherwise check that the binary representation of each number from
            n down to n//2+1 appears in s. Numbers ≤ n//2 are prefixes of
            larger numbers already verified.

        Complexity:
            Time: O(n * |s|) for substring checks
            Space: O(log n) for binary string conversion
        """
        if n > 1000:
            return False
        return all(bin(i)[2:] in s for i in range(n, n // 2, -1))
