class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """Sort and compare products of largest three vs two smallest with largest.

        Intuition:
        The maximum product of three numbers can come from either the three largest
        positive numbers or two most negative numbers multiplied by the largest positive.

        Approach:
        1. Sort the array.
        2. Compute the product of the three largest elements.
        3. Compute the product of the two smallest and the largest element.
        4. Return the maximum of both products.

        Complexity:
        Time: O(n log n)
        Space: O(1)
        """
        nums.sort()
        product_top_three = nums[-1] * nums[-2] * nums[-3]
        product_two_negatives = nums[-1] * nums[0] * nums[1]
        return max(product_top_three, product_two_negatives)
