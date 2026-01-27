from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """Add and subtract fractions using a common denominator approach.

        Intuition:
            Use a large common denominator (LCM of 1-10) to convert all
            fractions, sum them up, then simplify the result.

        Approach:
            1. Use 6*7*8*9*10 = 30240 as common denominator for all fractions.
            2. Prepend '+' if expression starts with a digit.
            3. Parse each fraction, convert to common denominator, and accumulate.
            4. Simplify the final fraction using GCD.

        Complexity:
            Time: O(n) where n is the expression length
            Space: O(1)
        """
        numerator, denominator = 0, 6 * 7 * 8 * 9 * 10
        if expression[0].isdigit():
            expression = "+" + expression
        i, length = 0, len(expression)
        while i < length:
            sign = -1 if expression[i] == "-" else 1
            i += 1
            j = i
            while j < length and expression[j] not in "+-":
                j += 1
            fraction_str = expression[i:j]
            frac_num, frac_den = fraction_str.split("/")
            numerator += sign * int(frac_num) * denominator // int(frac_den)
            i = j
        common = gcd(numerator, denominator)
        numerator //= common
        denominator //= common
        return f"{numerator}/{denominator}"
