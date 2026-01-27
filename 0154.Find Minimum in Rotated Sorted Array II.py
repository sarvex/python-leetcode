class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Binary Search with Duplicate Handling.

        Intuition:
            Similar to finding minimum in a rotated sorted array, but duplicates
            require shrinking the search space when mid equals the right boundary.

        Approach:
            Binary search comparing mid with the right boundary. If mid > right,
            minimum is in the right half. If mid < right, minimum is in the left
            half including mid. If equal, decrement right to eliminate the duplicate.

        Complexity:
            Time: O(log n) average, O(n) worst case with many duplicates
            Space: O(1) constant extra space
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
