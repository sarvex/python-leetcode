from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding Window - Find minimum size subarray with sum at least target

        Intuition:
        Instead of using prefix sums and binary search, we can use a sliding window
        approach to find the minimum subarray length. We maintain a window that
        expands to include elements until the sum is at least the target, then
        contracts from the left to minimize the window size.

        Approach:
        1. Use two pointers (left and right) to define the current window
        2. Expand the window by moving right pointer until sum >= target
        3. When sum >= target, record the window size and contract from left
        4. Continue this process until we've processed all elements

        Complexity:
        Time: O(n) where n is the length of nums - each element is processed at most twice
        Space: O(1) - only using a constant amount of extra space
        """
        n = len(nums)
        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(n):
            # Expand window from the right
            curr_sum += nums[right]

            # Contract window from the left while sum >= target
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
