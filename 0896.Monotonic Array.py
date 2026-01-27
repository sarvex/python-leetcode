from itertools import pairwise


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """Check both non-decreasing and non-increasing conditions.

        Intuition:
            An array is monotonic if it is entirely non-decreasing or
            entirely non-increasing. Check both conditions on adjacent pairs.

        Approach:
            1. Check if all consecutive pairs are non-decreasing.
            2. Check if all consecutive pairs are non-increasing.
            3. Return True if either condition holds.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        is_ascending = all(prev <= curr for prev, curr in pairwise(nums))
        is_descending = all(prev >= curr for prev, curr in pairwise(nums))
        return is_ascending or is_descending
