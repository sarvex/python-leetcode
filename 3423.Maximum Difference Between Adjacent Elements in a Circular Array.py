from typing import List
from itertools import pairwise

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        """Maximum difference between adjacent elements in a circular array.

        Intuition:
            For a circular array, we need to consider all adjacent pairs including
            the pair formed by the first and last elements. The maximum absolute
            difference between any adjacent pair will be our answer.

        Approach:
            1. Use pairwise to get all adjacent pairs in the original array
            2. Calculate absolute differences for all these pairs
            3. Also calculate the absolute difference between first and last element (circular connection)
            4. Return the maximum of all these differences

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(1) as we only use constant extra space
        """
        # Return maximum of all adjacent differences including the circular connection
        return max(
            max((abs(a - b) for a, b in pairwise(nums)), default=0),
            abs(nums[0] - nums[-1]) if len(nums) > 1 else 0
        )
