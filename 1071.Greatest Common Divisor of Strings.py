class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        GCD of Strings using mathematical GCD property

        Intuition:
        If str1 and str2 have a GCD string, then str1 + str2 must equal str2 + str1.
        The GCD string length will be the GCD of the lengths of the two strings.

        Approach:
        1. Check if str1 + str2 equals str2 + str1. If not, return empty string.
        2. Find the GCD of the lengths of str1 and str2 using Euclidean algorithm.
        3. Return the prefix of either string with length equal to the GCD.

        Complexity:
        Time: O(m+n) where m and n are lengths of str1 and str2
        Space: O(m+n) for string concatenation
        """
        # If strings don't have a GCD, concatenation test will fail
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths using Euclidean algorithm
        def gcd(a: int, b: int) -> int:
            """Calculate the greatest common divisor of two numbers."""
            return a if b == 0 else gcd(b, a % b)

        # The GCD string length is the GCD of the two string lengths
        gcd_length = gcd(len(str1), len(str2))

        # Return the prefix with length equal to the GCD
        return str1[:gcd_length]
