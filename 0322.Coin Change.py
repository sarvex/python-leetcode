from math import inf


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """2D unbounded knapsack DP for minimum coin count.

        Intuition:
            This is the classic unbounded knapsack problem where we want
            the minimum number of coins to make the target amount.

        Approach:
            1. Define dp[i][j] as the minimum coins using the first i coin types
               to make amount j.
            2. For each coin, either skip it (take from previous row) or use it
               (take from same row at j - coin_value, plus 1).
            3. Return dp[m][n] or -1 if unreachable.

        Complexity:
            Time: O(m * n) where m is number of coin types and n is amount
            Space: O(m * n) for the dp table
        """
        num_coins, target = len(coins), amount
        dp = [[inf] * (target + 1) for _ in range(num_coins + 1)]
        dp[0][0] = 0
        for i, coin in enumerate(coins, 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coin:
                    dp[i][j] = min(dp[i][j], dp[i][j - coin] + 1)
        return -1 if dp[num_coins][target] >= inf else dp[num_coins][target]
