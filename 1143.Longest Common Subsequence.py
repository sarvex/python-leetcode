from itertools import product


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Dynamic programming approach to find the length of longest common subsequence.

        Intuition:
            For each position in both strings, we have two cases:
            1. If characters match, we extend the LCS from previous positions
            2. If they don't match, we take the best result from skipping either character

        Approach:
            Use a 2D DP table where dp[i][j] represents the length of the LCS
            of text1[0...i-1] and text2[0...j-1]. Fill this table bottom-up.

        Complexity:
            Time: O(m*n) where m and n are the lengths of the input strings
            Space: O(m*n) for the DP table
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, j in product(range(1, m + 1), range(1, n + 1)):
            dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    def longestCommonSubsequence_optimized(self, text1: str, text2: str) -> int:
        """Space-optimized dynamic programming solution.

        Intuition:
            We only need the previous row of the DP table to calculate the current row,
            so we can optimize the space complexity.

        Approach:
            Use two 1D arrays (current and previous) instead of a full 2D table.
            After processing each row, the current row becomes the previous row.

        Complexity:
            Time: O(m*n) where m and n are the lengths of the input strings
            Space: O(min(m,n)) as we only store two rows
        """
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr[j] = prev[j - 1] + 1 if text1[i - 1] == text2[j - 1] else max(prev[j], curr[j - 1])
            prev, curr = curr, prev

        return prev[n]

    def longestCommonSubsequence_further_optimized(self, text1: str, text2: str) -> int:
        """Further space-optimized solution using a single array.

        Intuition:
            We can optimize even further by using a single array and updating it in-place,
            but we need to be careful about the order of updates.

        Approach:
            Use a single 1D array and update it from right to left in each iteration
            to avoid overwriting values we still need.

        Complexity:
            Time: O(m*n) where m and n are the lengths of the input strings
            Space: O(min(m,n)) for the single array
        """
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                current = dp[j]
                dp[j] = prev + 1 if text1[i - 1] == text2[j - 1] else max(dp[j], dp[j - 1])
                prev = current

        return dp[n]
