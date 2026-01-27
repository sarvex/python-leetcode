from collections import deque
from math import inf


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        """Find maximum sum subsequence where adjacent indices differ by at most k.

        Intuition:
            Use DP with a monotonic deque to efficiently query the maximum
            DP value within the last k positions.

        Approach:
            For each position, dp[i] = nums[i] + max(0, max dp[j] for j in
            [i-k, i-1]). Use a decreasing deque to maintain the maximum
            in the sliding window of size k.

        Complexity:
            Time: O(n) each element enters and leaves the deque once
            Space: O(n) for the DP array and deque
        """
        length = len(nums)
        dp = [0] * length
        result = -inf
        window: deque[int] = deque()
        for i, value in enumerate(nums):
            if window and i - window[0] > k:
                window.popleft()
            dp[i] = max(0, 0 if not window else dp[window[0]]) + value
            while window and dp[window[-1]] <= dp[i]:
                window.pop()
            window.append(i)
            result = max(result, dp[i])
        return int(result)
