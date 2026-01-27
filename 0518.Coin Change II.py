class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """Unbounded knapsack DP to count combinations summing to amount.

        Intuition:
            This is an unbounded knapsack problem where each coin can be used
            unlimited times. We count the number of ways to make the amount.

        Approach:
            Use 2D DP where dp[i][j] = number of ways to make amount j using
            first i coin types. Each coin can be included (unbounded) or excluded.

        Complexity:
            Time: O(m * n) where m = len(coins), n = amount
            Space: O(m * n)
        """
        num_coins, target = len(coins), amount
        dp = [[0] * (target + 1) for _ in range(num_coins + 1)]
        dp[0][0] = 1
        for i, coin in enumerate(coins, 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]
        return dp[num_coins][target]
