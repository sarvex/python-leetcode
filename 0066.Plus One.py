from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Digit-by-digit addition with carry propagation

        Intuition:
        When adding 1 to a number represented as an array of digits, we need to
        start from the least significant digit (rightmost) and handle any carry
        that might propagate to more significant digits.

        Approach:
        1. Iterate through the digits from right to left
        2. Add 1 to the current digit
        3. Take modulo 10 to handle carry (if digit becomes 10, it becomes 0)
        4. If the result is not 0, there's no carry, so return immediately
        5. If we exit the loop, it means we had carries all the way through
           (e.g., 999 + 1), so we need to add a new leading digit 1

        Complexity:
        Time: O(n) where n is the number of digits
        Space: O(1) if we don't count the output, O(n) if we do
        """
        n = len(digits)

        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits

        # If we reach here, it means we had all 9's
        return [1] + digits
