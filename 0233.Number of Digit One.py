from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        """Digit DP with memoization to count occurrences of digit one.

        Intuition:
            Use digit dynamic programming to count how many times '1' appears
            in all numbers from 1 to n by processing each digit position.

        Approach:
            1. Extract digits of n into an array.
            2. Define a recursive function with position, count of ones, and
               whether we are still bounded by n's digits.
            3. At each position, try all valid digits and accumulate counts.

        Complexity:
            Time: O(log(n) * log(n) * 10) for digit positions and states
            Space: O(log(n)^2) for memoization
        """

        @cache
        def dfs(position: int, ones_count: int, is_limited: bool) -> int:
            if position <= 0:
                return ones_count
            upper_bound = digits[position] if is_limited else 9
            total = 0
            for digit in range(upper_bound + 1):
                total += dfs(
                    position - 1,
                    ones_count + (digit == 1),
                    is_limited and digit == upper_bound,
                )
            return total

        digits = [0] * 12
        num_digits = 1
        while n:
            digits[num_digits] = n % 10
            n //= 10
            num_digits += 1
        return dfs(num_digits, 0, True)
