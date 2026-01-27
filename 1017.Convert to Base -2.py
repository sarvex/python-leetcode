class Solution:
    def baseNeg2(self, n: int) -> str:
        """Convert an integer to its base -2 representation.

        Intuition:
            Division with negative base works similarly to positive base, but
            the remainder must always be non-negative, adjusting the quotient
            accordingly.

        Approach:
            Repeatedly extract the least significant bit. If the current value
            is odd, record '1' and subtract the current sign factor. Divide by
            2 and flip the sign factor each iteration.

        Complexity:
            Time: O(log n) for processing each bit
            Space: O(log n) for the result digits
        """
        sign = 1
        digits: list[str] = []
        while n:
            if n % 2:
                digits.append("1")
                n -= sign
            else:
                digits.append("0")
            n //= 2
            sign *= -1
        return "".join(reversed(digits)) or "0"
