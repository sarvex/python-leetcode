class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Binary exponentiation for efficient power calculation

        Intuition:
        Computing x^n naively requires n multiplications, but we can do better
        using binary exponentiation (also known as exponentiation by squaring).

        Approach:
        1. Handle negative exponents by computing 1/x^|n|
        2. Use binary exponentiation: break n into powers of 2
        3. For each bit in n's binary representation, multiply result by x^(2^i) if bit is 1

        Complexity:
        Time: O(log n) - We only need log(n) multiplications
        Space: O(1) - Constant extra space used
        """
        def binary_exponentiation(base: float, exponent: int) -> float:
            result = 1.0
            while exponent:
                if exponent & 1:  # If current bit is 1
                    result *= base
                base *= base  # Square the base
                exponent >>= 1  # Move to next bit
            return result

        return binary_exponentiation(x, n) if n >= 0 else 1 / binary_exponentiation(x, -n)
