class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """LIS-style DP on columns to find longest non-decreasing subsequence.

        Intuition:
            We need to find the longest subsequence of columns such that each
            row remains sorted. This is analogous to Longest Increasing Subsequence
            but across all rows simultaneously.

        Approach:
            1. For each column i, dp[i] = length of longest valid column subsequence ending at i.
            2. Column j can extend column i's subsequence if strs[row][j] <= strs[row][i] for all rows.
            3. Answer is total columns minus the longest valid subsequence.

        Complexity:
            Time: O(n^2 * m) — n = number of columns, m = number of rows
            Space: O(n) — DP array
        """
        num_cols = len(strs[0])
        dp = [1] * num_cols
        for col in range(1, num_cols):
            for prev_col in range(col):
                if all(row[prev_col] <= row[col] for row in strs):
                    dp[col] = max(dp[col], dp[prev_col] + 1)
        return num_cols - max(dp)
