from typing import List
from math import inf


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """Maximum difference between increasing elements.

        Intuition:
        Find the maximum difference between any two elements where the larger element
        appears after the smaller element in the array.

        Approach:
        Keep track of the minimum element encountered so far and calculate the maximum
        difference when we find a larger element. If no valid pair exists, return -1.

        Complexity:
        Time: O(n) where n is the length of nums - single pass through the array
        Space: O(1) - constant extra space used
        """
        min_val = inf
        max_diff = -1

        for num in nums:
            if num > min_val:
                max_diff = max(max_diff, num - min_val)
            else:
                min_val = num

        return max_diff
