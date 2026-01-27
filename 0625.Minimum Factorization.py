class Solution:
    def smallestFactorization(self, num: int) -> int:
        """Find smallest positive integer whose digits multiply to num.

        Intuition:
            Greedily extract the largest single-digit factors (9 down to 2)
            to minimize the number of digits, placing larger factors in less
            significant positions to get the smallest number.

        Approach:
            1. Handle base case where num < 2 (return num directly).
            2. Try dividing by digits 9 down to 2, building the result by
               placing each factor at increasing decimal positions.
            3. If num is not fully reduced to 1, return 0 (no valid answer).
            4. Check for 32-bit integer overflow.

        Complexity:
            Time: O(log num) since each division reduces num
            Space: O(1)
        """
        if num < 2:
            return num
        result, multiplier = 0, 1
        for digit in range(9, 1, -1):
            while num % digit == 0:
                num //= digit
                result = multiplier * digit + result
                multiplier *= 10
        return result if num < 2 and result <= 2**31 - 1 else 0
