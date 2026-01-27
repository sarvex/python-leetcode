class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """Find minimum cost to guarantee a win using interval DP.

        Intuition:
            For any range [i, j], guessing k costs k plus the worst case of
            the two remaining subproblems [i, k-1] and [k+1, j]. We want
            to minimize the worst-case cost over all possible guesses.

        Approach:
            Use bottom-up interval DP. For each interval [i, j], try every
            possible guess k and compute cost as k + max(dp[i][k-1], dp[k+1][j]).
            Take the minimum over all k. Process intervals from smaller to larger.

        Complexity:
            Time: O(n^3)
            Space: O(n^2)
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = j + dp[i][j - 1]
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k - 1], dp[k + 1][j]) + k)
        return dp[1][n]
