class Solution:
    def convertToBase7(self, num: int) -> str:
        """Convert integer to base 7 string representation.

        Intuition:
            Repeatedly divide by 7 and collect remainders, similar to any
            base conversion algorithm.

        Approach:
            Handle zero and negative cases. Repeatedly take modulo 7 and
            integer divide by 7, collecting digits in reverse order.

        Complexity:
            Time: O(log num)
            Space: O(log num)
        """
        if num == 0:
            return "0"
        if num < 0:
            return "-" + self.convertToBase7(-num)
        digits: list[str] = []
        while num:
            digits.append(str(num % 7))
            num //= 7
        return "".join(digits[::-1])
