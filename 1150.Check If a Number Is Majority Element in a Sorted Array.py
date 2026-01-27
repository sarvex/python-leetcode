from bisect import bisect_left, bisect_right


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        """Check if target appears more than len(nums) // 2 times.

        Intuition:
            Since the array is sorted, all occurrences of target are
            contiguous. Binary search can find the range efficiently.

        Approach:
            Use bisect_left and bisect_right to find the first and last
            positions of target. The count is the difference, which is
            compared against half the array length.

        Complexity:
            Time: O(log n) where n is the length of nums
            Space: O(1)
        """
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return right - left > len(nums) // 2
