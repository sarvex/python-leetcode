class Solution:
    def mySqrt(self, x: int) -> int:
        """Binary Search Approach

        Intuition:
            The square root of x is the largest integer whose square is <= x.
            This naturally fits a binary search on the answer space.

        Approach:
            Use binary search between 0 and x. For each midpoint, check if
            mid * mid exceeds x. If it does, shrink the right boundary;
            otherwise, move the left boundary up. The upper-biased midpoint
            formula avoids infinite loops when left and right differ by 1.

        Complexity:
            Time: O(log x)
            Space: O(1)
        """
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) >> 1
            if mid > x // mid:
                right = mid - 1
            else:
                left = mid
        return left
