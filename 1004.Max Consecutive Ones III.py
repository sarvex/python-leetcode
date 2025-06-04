from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Sliding window approach for maximum consecutive ones with flips

        Intuition:
        Use a sliding window to track a segment where we can have at most k zeros.
        When we exceed k zeros, shrink the window from the left until we're valid again.

        Approach:
        1. Use a sliding window with two pointers (left and right)
        2. Expand window to the right, counting zeros encountered
        3. When zeros exceed k, shrink window from left until valid
        4. The window size at the end represents the longest valid subarray

        Complexity:
        Time: O(n) where n is the length of nums, each element is processed at most twice
        Space: O(1) as we only use a constant amount of extra space
        """
        left = zero = 0

        for num in nums:
            if num == 0:
                zero += 1

            if zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1

        return len(nums) - left
