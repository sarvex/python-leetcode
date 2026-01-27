class Solution:
    def trailingZeroes(self, n: int) -> int:
        """Count trailing zeroes by counting factors of 5.

        Intuition:
            Trailing zeroes come from factors of 10, which is 2 * 5. Since
            factors of 2 are always more abundant, counting factors of 5
            suffices.

        Approach:
            1. Repeatedly divide n by 5.
            2. Accumulate the quotient each time (counts multiples of 5, 25,
               125, etc.).

        Complexity:
            Time: O(log₅ n)
            Space: O(1)
        """
        count = 0
        while n:
            n //= 5
            count += n
        return count
