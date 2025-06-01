class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Bit manipulation approach to divide two integers without using multiplication, division, or mod

        Intuition:
        Since we can't use multiplication, division, or modulo operators, we need to
        implement division using subtraction. However, naive repeated subtraction would be
        too slow. Instead, we can use bit manipulation to perform exponential subtraction.

        Approach:
        1. Handle edge cases: division by 1, and overflow case (MIN_INT / -1)
        2. Determine the sign of the result
        3. Convert both numbers to negative to handle MIN_INT edge case uniformly
        4. For each step:
           - Find the largest multiple of divisor (x) that can be subtracted from dividend
           - Subtract x from dividend and add the corresponding count to the result
           - Repeat until dividend is smaller than divisor
        5. Apply the correct sign to the result

        Complexity:
        Time: O(log(dividend)) - we double the value in each inner loop iteration
        Space: O(1) - only using constant extra space
        """
        # Handle edge cases
        if divisor == 1:
            return dividend

        # Handle overflow case: -2^31 / -1 = 2^31 which exceeds the 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative_result = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)

        # Convert both numbers to negative to handle MIN_INT edge case
        # (since abs(MIN_INT) would overflow in a 32-bit integer)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor

        result = 0
        while dividend <= divisor:
            # Find largest multiple of divisor that fits into the current dividend
            current_divisor = divisor
            multiple = 1

            # Keep doubling the divisor until it would exceed the dividend
            # We check against -2^30 to prevent potential overflow
            while current_divisor >= INT_MIN // 2 and dividend <= current_divisor + current_divisor:
                current_divisor <<= 1  # Double the divisor
                multiple <<= 1         # Double the count

            # Subtract the largest valid multiple of divisor from dividend
            dividend -= current_divisor
            result += multiple

        return -result if negative_result else result
