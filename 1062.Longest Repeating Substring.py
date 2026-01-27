class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        """Find the length of the longest repeating substring.

        Intuition:
            Use dynamic programming to compare all pairs of starting positions
            for matching substrings.

        Approach:
            Build a 2D DP table where dp[i][j] is the length of the common
            substring ending at s[i] and s[j] (with i < j). Track the maximum.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i else 1
                    result = max(result, dp[i][j])
        return result
