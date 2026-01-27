class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """Dynamic Programming with Min/Max Tracking.

        Intuition:
            A negative number can turn the smallest product into the largest,
            so we need to track both the current maximum and minimum products.

        Approach:
            Maintain running maximum and minimum products at each position.
            For each number, compute new max and min considering the current
            number alone or multiplied with previous max/min. Update the
            global answer with the running maximum.

        Complexity:
            Time: O(n) single pass through the array
            Space: O(1) only tracking max and min products
        """
        result = max_product = min_product = nums[0]
        for num in nums[1:]:
            prev_max, prev_min = max_product, min_product
            max_product = max(num, prev_max * num, prev_min * num)
            min_product = min(num, prev_max * num, prev_min * num)
            result = max(result, max_product)
        return result
