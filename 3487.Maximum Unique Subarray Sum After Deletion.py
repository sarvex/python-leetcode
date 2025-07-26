from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Optimized greedy selection using set conversion for unique elements.

        Intuition:
        Since we can delete any elements, we should keep only non-negative unique
        elements to maximize the sum. Converting to set first eliminates duplicates
        efficiently, then we sum only non-negative values.

        Approach:
        1. Handle edge case where all elements are negative
        2. Convert array to set to eliminate duplicates in O(n) time
        3. Sum only non-negative unique elements

        Complexity:
        Time: O(n) - set conversion and iteration
        Space: O(k) - set storage for unique elements
        """
        # Handle edge case: if all elements are negative, return the maximum
        if max(nums) < 0:
            return max(nums)

        # Convert to set to eliminate duplicates, then sum non-negative elements
        return sum(num for num in frozenset(nums) if num >= 0)
