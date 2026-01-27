class Solution:
    def isUgly(self, n: int) -> bool:
        """Iteratively divide by prime factors 2, 3, and 5 to check ugly number.

        Intuition:
            An ugly number only has prime factors 2, 3, and 5. By repeatedly
            dividing out these factors, a truly ugly number reduces to 1.

        Approach:
            1. Return False for non-positive numbers.
            2. Repeatedly divide n by 2, 3, and 5 while divisible.
            3. If the result is 1, n is ugly; otherwise it is not.

        Complexity:
            Time: O(log n) for the divisions
            Space: O(1)
        """
        if n < 1:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1
