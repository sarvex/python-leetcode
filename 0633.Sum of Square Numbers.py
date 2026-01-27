from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """Two-pointer approach to find two squares summing to c.

        Intuition:
        Use two pointers starting at 0 and sqrt(c). Adjust pointers based on
        whether the current sum of squares is less than, equal to, or greater than c.

        Approach:
        1. Initialize left = 0 and right = floor(sqrt(c)).
        2. Compute left^2 + right^2.
        3. If equal to c, return True.
        4. If less, increment left; if greater, decrement right.
        5. If pointers cross, return False.

        Complexity:
        Time: O(sqrt(c))
        Space: O(1)
        """
        left, right = 0, isqrt(c)
        while left <= right:
            total = left**2 + right**2
            if total == c:
                return True
            if total < c:
                left += 1
            else:
                right -= 1
        return False
