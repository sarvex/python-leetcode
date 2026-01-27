from functools import cache


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        """Top-Down DP with Memoization Approach

        Intuition:
            Use recursive DFS with memoization to explore all buy/sell
            decisions while tracking the number of remaining transactions.

        Approach:
            1. Define a recursive function with state: index, remaining
               transactions, and whether currently holding a stock.
            2. At each step, either skip or buy/sell depending on state.
            3. Cache results to avoid recomputation.

        Complexity:
            Time: O(n * k) where n is the number of prices
            Space: O(n * k) for the memoization cache
        """

        @cache
        def dfs(index: int, remaining: int, holding: int) -> int:
            if index >= len(prices):
                return 0
            profit = dfs(index + 1, remaining, holding)
            if holding:
                profit = max(profit, prices[index] + dfs(index + 1, remaining, 0))
            elif remaining:
                profit = max(profit, -prices[index] + dfs(index + 1, remaining - 1, 1))
            return profit

        return dfs(0, k, 0)
