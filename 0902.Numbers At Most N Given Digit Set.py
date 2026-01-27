from functools import cache


class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        """Digit DP with memoization counting valid numbers up to n.

        Intuition:
            Use digit DP to count numbers up to n where each digit belongs
            to the given set. Track leading zeros and tight constraint.

        Approach:
            1. Decompose n into its digits (stored in reverse for positional access).
            2. Define a recursive function with position, leading-zero flag,
               and tight-constraint flag.
            3. For each position, try all digits 0-9 that are in the allowed set
               (or 0 if still in leading-zero state).
            4. Memoize on (position, leading_zero, is_tight).

        Complexity:
            Time: O(L * |digits| * 10) where L is the number of digits in n.
            Space: O(L)
        """
        allowed_digits = {int(d) for d in digits}
        digit_array = [0] * 12
        num_digits = 0
        while n:
            num_digits += 1
            digit_array[num_digits] = n % 10
            n //= 10

        @cache
        def dfs(position: int, has_leading_zero: bool, is_tight: bool) -> int:
            if position <= 0:
                return 0 if has_leading_zero else 1
            upper_bound = digit_array[position] if is_tight else 9
            count = 0
            for digit in range(upper_bound + 1):
                if digit == 0 and has_leading_zero:
                    count += dfs(
                        position - 1,
                        has_leading_zero,
                        is_tight and digit == upper_bound,
                    )
                elif digit in allowed_digits:
                    count += dfs(position - 1, False, is_tight and digit == upper_bound)
            return count

        return dfs(num_digits, True, True)
