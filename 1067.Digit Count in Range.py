from functools import cache


class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        """Count occurrences of digit d in range [low, high].

        Intuition:
            Use digit DP to count occurrences of a digit up to a number, then
            apply subtraction: f(high) - f(low - 1).

        Approach:
            Digit DP with memoization tracking position, count of d seen,
            leading zero status, and tight constraint.

        Complexity:
            Time: O(log(high) * 10) for digit DP states
            Space: O(log(high)) for recursion and memoization
        """
        return self._count_up_to(high, d) - self._count_up_to(low - 1, d)

    def _count_up_to(self, n: int, d: int) -> int:
        """Count occurrences of digit d in all numbers from 1 to n."""

        @cache
        def dfs(pos: int, count: int, leading_zero: bool, tight: bool) -> int:
            if pos <= 0:
                return count
            upper = digits[pos] if tight else 9
            total = 0
            for digit in range(upper + 1):
                if digit == 0 and leading_zero:
                    total += dfs(pos - 1, count, leading_zero, tight and digit == upper)
                else:
                    total += dfs(
                        pos - 1, count + (digit == d), False, tight and digit == upper
                    )
            return total

        digits = [0] * 11
        length = 0
        while n:
            length += 1
            digits[length] = n % 10
            n //= 10
        return dfs(length, 0, True, True)
