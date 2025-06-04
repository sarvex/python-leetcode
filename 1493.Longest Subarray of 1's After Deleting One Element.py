from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """One-pass sliding window with constant space for maximum subarray after deleting one element.

        Intuition:
        Maintain a window with at most one zero, tracking the longest valid subarray length.

        Approach:
        Use a single-pass sliding window that expands when possible and contracts when we exceed
        our zero allowance. We directly shift the left pointer when needed instead of using a while loop.

        Complexity:
        Time: O(n) where n is the length of nums - single pass with O(1) operations per element
        Space: O(1) - only using a few variables regardless of input size
        """
        n = len(nums)
        if n <= 1:
            return 0

        left = zeros = result = 0

        for right in range(n):
            zeros += nums[right] == 0

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            result = max(result, right - left)

        return min(result, n - 1)
