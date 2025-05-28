from bisect import bisect_left
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Binary search approach to find first and last position of target.
        
        Intuition:
            Using binary search to efficiently find the target's positions.
            The first position is where target first appears.
            The last position is right before where (target+1) would appear.
        
        Approach:
            1. Use bisect_left to find the leftmost insertion point for target
            2. Use bisect_left again to find the leftmost insertion point for (target+1)
            3. If target exists, the range is [left_index, right_index-1]
            4. If target doesn't exist, return [-1, -1]
        
        Complexity:
            Time: O(log n) where n is the length of nums
            Space: O(1) as we only use constant extra space
        """
        left = bisect_left(nums, target)
        right = bisect_left(nums, target + 1)
        
        # If left equals right, target doesn't exist in the array
        return [-1, -1] if left == right else [left, right - 1]
