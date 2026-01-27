class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        """Longest Arithmetic Subsequence using dynamic programming.

        Intuition:
            For each pair of elements, track the length of the arithmetic
            subsequence ending at that element with a given common difference.

        Approach:
            Use a 2D DP table where f[i][d] represents the longest arithmetic
            subsequence ending at index i with difference d (offset by 500 to
            handle negative differences). For each pair (k, i), update
            f[i][nums[i]-nums[k]+500] from f[k][same_diff] + 1.

        Complexity:
            Time: O(n^2)
            Space: O(n * 1001)
        """
        length = len(nums)
        dp = [[1] * 1001 for _ in range(length)]
        result = 0
        for i in range(1, length):
            for k in range(i):
                diff = nums[i] - nums[k] + 500
                dp[i][diff] = max(dp[i][diff], dp[k][diff] + 1)
                result = max(result, dp[i][diff])
        return result
