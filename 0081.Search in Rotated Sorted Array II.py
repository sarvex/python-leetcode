class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """Modified Binary Search with Duplicate Handling

        Intuition:
            Similar to searching in a rotated sorted array, but duplicates
            can make it impossible to determine which half is sorted. When
            nums[mid] == nums[right], shrink the right boundary by one.

        Approach:
            Use binary search. If nums[mid] > nums[right], the left half
            is sorted—check if target lies within it. If nums[mid] < nums[right],
            the right half is sorted—check if target lies within it. If equal,
            decrement right to skip the duplicate.

        Complexity:
            Time: O(n) worst case, O(log n) average
            Space: O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                right -= 1
        return nums[left] == target
