from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Two-pass approach with O(1) extra space

        Intuition:
        Instead of using division, we can compute the product of all elements to the left
        of each element, then multiply by the product of all elements to the right.

        Approach:
        1. First pass: Calculate products of all elements to the left of each element
        2. Second pass: Multiply each element by the product of all elements to its right

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) extra space (excluding the output array)
        """
        n = len(nums)
        result = [1] * n

        # First pass: Calculate products of all elements to the left
        left_product = 1
        for i, num in enumerate(nums):
            result[i] = left_product
            left_product *= num

        # Second pass: Multiply by products of all elements to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
