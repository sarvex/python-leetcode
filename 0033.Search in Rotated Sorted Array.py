from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search in rotated sorted array

        Intuition:
        In a rotated sorted array, there's always one half that is sorted.
        By comparing with the endpoints, we can determine which half is sorted,
        then check if the target is in that sorted half.

        Approach:
        1. Use binary search to find the target
        2. For each mid point, determine which half is sorted
        3. Check if target is in the sorted half, otherwise search in the other half
        4. Continue until we find the target or exhaust the search space

        Complexity:
        Time: O(log n) - Binary search reduces search space by half each iteration
        Space: O(1) - Only using constant extra space for variables
        """
        if not nums:
            return -1

        array_length = len(nums)
        left, right = 0, array_length - 1

        while left < right:
            mid = (left + right) >> 1

            # Check if left half is sorted
            if nums[0] <= nums[mid]:
                # If target is in the sorted left half
                if nums[0] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # Right half is sorted
                # If target is in the sorted right half
                if nums[mid] < target <= nums[array_length - 1]:
                    left = mid + 1
                else:
                    right = mid

        # Check if the final position contains the target
        return left if left < array_length and nums[left] == target else -1
