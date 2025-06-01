from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Binary search to find insert position

        Intuition:
        Since the array is sorted, we can use binary search to efficiently find the position
        where the target should be inserted. If the target exists, return its index;
        otherwise, return the index where it would be inserted to maintain the sorted order.

        Approach:
        1. Use binary search with two pointers (left and right)
        2. While left < right, calculate the middle index
        3. If nums[mid] >= target, move right pointer to mid
        4. Otherwise, move left pointer to mid + 1
        5. Return the left pointer as the insert position

        Complexity:
        Time: O(log n) where n is the length of the array
        Space: O(1) constant extra space
        """
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) >> 1  # Equivalent to floor division by 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left
