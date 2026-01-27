class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """Sliding window to count subarrays with product less than k.

        Intuition:
            Maintain a window where the product of all elements is less than k.
            As we expand the right boundary, shrink the left boundary when the
            product becomes too large.

        Approach:
            1. Use two pointers (left, right) defining a sliding window.
            2. Expand right pointer, multiplying the product by the new element.
            3. While product >= k, divide by the left element and advance left.
            4. Each valid window of size (right - left + 1) contributes that
               many new subarrays ending at right.

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(1)
        """
        count, product, left = 0, 1, 0
        for right, value in enumerate(nums):
            product *= value
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count
