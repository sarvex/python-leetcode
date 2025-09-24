class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """Tagline: Convert a fraction to its decimal string with recurring part in parentheses

        Intuition:
        Do long division and track previously seen remainders. The first repeated
        remainder indicates the start of the recurring cycle.

        Approach:
        - Handle zero numerator early.
        - Determine sign via XOR of input signs.
        - Use absolute values to compute the integer part and the initial remainder.
        - If the remainder is zero, return the integer part.
        - Otherwise, append a decimal point and simulate long division:
          map remainder -> position in the output list. On repetition, insert '('
          at the stored position and append ')' to close the cycle.

        Complexity:
        Time: O(k), where k is the number of produced decimal digits
        Space: O(k), for the output buffer and remainder index map
        """
        if numerator == 0:
            return "0"

        parts: list[str] = []
        is_negative = (numerator > 0) ^ (denominator > 0)
        if is_negative:
            parts.append("-")

        n, d = abs(numerator), abs(denominator)
        parts.append(str(n // d))
        remainder = n % d
        if remainder == 0:
            return "".join(parts)

        parts.append(".")
        seen: dict[int, int] = {}
        while remainder != 0 and remainder not in seen:
            seen[remainder] = len(parts)
            remainder *= 10
            parts.append(str(remainder // d))
            remainder %= d

        if remainder in seen:
            parts.insert(seen[remainder], "(")
            parts.append(")")

        return "".join(parts)
