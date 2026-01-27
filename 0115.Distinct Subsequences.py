class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """2D Dynamic Programming

        Intuition:
            Count the number of ways to form t as a subsequence of s. At each
            character pair, we either skip the current character of s or, if
            characters match, also count the ways where both characters are used.

        Approach:
            Build a 2D DP table where dp[i][j] represents the number of
            distinct subsequences of s[:i] that equal t[:j]. Base case:
            dp[i][0] = 1 (empty t matches any prefix). For each character
            pair, dp[i][j] = dp[i-1][j] (skip s[i-1]). If s[i-1] == t[j-1],
            also add dp[i-1][j-1].

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        len_s, len_t = len(s), len(t)
        dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
        for i in range(len_s + 1):
            dp[i][0] = 1
        for i, char_s in enumerate(s, 1):
            for j, char_t in enumerate(t, 1):
                dp[i][j] = dp[i - 1][j]
                if char_s == char_t:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[len_s][len_t]
