class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Classic binary search on a sorted array.

        Intuition:
            A sorted array allows halving the search space each step by
            comparing the middle element with the target.

        Approach:
            1. Use two pointers for the search range.
            2. Compare the middle element with the target.
            3. Narrow the range to the left or right half accordingly.
            4. Return the index if found, otherwise -1.

        Complexity:
            Time: O(log n) halving the search space each iteration
            Space: O(1) constant extra space
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1
