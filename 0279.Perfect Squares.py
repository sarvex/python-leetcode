from math import inf, sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        """Dynamic programming with complete knapsack pattern.

        Intuition:
            Each perfect square can be used unlimited times, making this a
            classic unbounded knapsack problem where we find the minimum
            count of perfect squares summing to n.

        Approach:
            1. Compute m = floor(sqrt(n)) to identify all usable perfect squares.
            2. Build a 2D DP table where dp[i][j] represents the minimum number
               of perfect squares from the first i squares that sum to j.
            3. For each square i*i, either skip it or use it (reducing j by i*i).
            4. Return dp[m][n].

        Complexity:
            Time: O(m * n) where m = sqrt(n)
            Space: O(m * n)
        """
        max_square = int(sqrt(n))
        dp = [[inf] * (n + 1) for _ in range(max_square + 1)]
        dp[0][0] = 0
        for i in range(1, max_square + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= i * i:
                    dp[i][j] = min(dp[i][j], dp[i][j - i * i] + 1)
        return dp[max_square][n]
