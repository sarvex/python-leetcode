from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Binary search to find a peak element in the array.

        Intuition:
        If we're at position i and nums[i] > nums[i+1], then there must be a peak
        element to the left of or at position i. Conversely, if nums[i] < nums[i+1],
        then there must be a peak element to the right of position i.

        Approach:
        Use binary search to find a position where nums[i] > nums[i+1]. The search
        space is continuously narrowed by comparing the middle element with its
        adjacent element to determine which half contains a peak.

        Complexity:
        Time: O(log n) where n is the length of the array
        Space: O(1) constant extra space
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                # Peak is in the left half or at mid
                right = mid
            else:
                # Peak is in the right half
                left = mid + 1

        return left
