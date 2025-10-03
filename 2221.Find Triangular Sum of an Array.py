from math import comb


class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        """
        Optimized combinatorial approach using binomial coefficients.

        Intuition:
        Instead of simulating the reduction process, observe that each element
        contributes to the final result with a weight equal to C(n-1, i), where
        n is array length and i is the element's index.

        Approach:
        Calculate the weighted sum of all elements using binomial coefficients.
        Each nums[i] contributes nums[i] * C(n-1, i) to the final result.

        Complexity:
        Time: O(n) - single pass through array with O(1) comb calculation
        Space: O(1) - only using constant extra space
        """
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            res += num * comb(n - 1, i)

        return res % 10
