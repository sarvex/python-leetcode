class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """3D DP knapsack with zero and one count constraints.

        Intuition:
            This is a variant of the 0/1 knapsack problem with two capacity
            dimensions: the count of zeros and the count of ones.

        Approach:
            For each string, count its zeros and ones. Use a 3D DP table
            where dp[i][j][k] represents the max subset size using the
            first i strings with at most j zeros and k ones. For each
            string, either skip it or include it if capacity allows.

        Complexity:
            Time: O(len(strs) * m * n)
            Space: O(len(strs) * m * n)
        """
        size = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(size + 1)]
        for i, string in enumerate(strs, 1):
            zero_count, one_count = string.count("0"), string.count("1")
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zero_count and k >= one_count:
                        dp[i][j][k] = max(
                            dp[i][j][k], dp[i - 1][j - zero_count][k - one_count] + 1
                        )
        return dp[size][m][n]
