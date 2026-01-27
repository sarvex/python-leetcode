class Solution:
    def findMin(self, nums: list[int]) -> int:
        """Binary Search on Rotated Array.

        Intuition:
            In a rotated sorted array, the minimum element is at the rotation
            point. Binary search can find it by comparing with the first element.

        Approach:
            If the array is not rotated (first <= last), return the first element.
            Otherwise, binary search: if mid is >= first element, the rotation
            point is to the right; otherwise it is to the left (including mid).

        Complexity:
            Time: O(log n) binary search
            Space: O(1) constant extra space
        """
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
