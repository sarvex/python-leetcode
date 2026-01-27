class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        """Compute a^b mod 1337 where b is represented as an array of digits.

        Intuition:
            Process digits of the exponent from least significant to most
            significant. Each digit contributes a^(digit) with the base
            raised to the power of 10 for each subsequent position.

        Approach:
            Iterate through the digits of b in reverse. For each digit,
            multiply the result by a^digit mod 1337, then raise a to the
            10th power mod 1337 for the next position.

        Complexity:
            Time: O(n) where n is the number of digits in b
            Space: O(1)
        """
        mod = 1337
        result = 1
        for exponent in b[::-1]:
            result = result * pow(a, exponent, mod) % mod
            a = pow(a, 10, mod)
        return result
