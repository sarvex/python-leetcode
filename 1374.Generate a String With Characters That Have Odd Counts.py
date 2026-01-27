class Solution:
    def generateTheString(self, n: int) -> str:
        """Generate a string of length n where every character has an odd count.

        Intuition:
            If n is odd, use a single character repeated n times. If n is even,
            use one character n-1 times (odd) and a different character once (odd).

        Approach:
            Check parity of n. Return n copies of 'a' if odd, otherwise n-1
            copies of 'a' plus one 'b'.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        return "a" * n if n & 1 else "a" * (n - 1) + "b"
