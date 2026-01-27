from math import inf


class Solution:
    def strangePrinter(self, s: str) -> int:
        """Interval DP to minimize print turns for a strange printer.

        Intuition:
        If s[i] == s[j], the printer can print the last character for free during
        the first character's turn, so dp[i][j] = dp[i][j-1]. Otherwise, try
        all split points.

        Approach:
        1. Define dp[i][j] as minimum turns to print s[i..j].
        2. Base case: dp[i][i] = 1 (single character).
        3. If s[i] == s[j], dp[i][j] = dp[i][j-1].
        4. Otherwise, dp[i][j] = min(dp[i][k] + dp[k+1][j]) for all split points k.

        Complexity:
        Time: O(n^3)
        Space: O(n^2)
        """
        length = len(s)
        dp = [[inf] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][-1]
