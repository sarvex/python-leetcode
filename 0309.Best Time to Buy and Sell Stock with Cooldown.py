from functools import cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Top-down DP with memoization tracking holding state.

        Intuition:
            At each day, we either hold a stock or not. If holding, we can sell
            (with a cooldown). If not holding, we can buy.

        Approach:
            1. Define dfs(i, is_holding) as the max profit from day i onward.
            2. If holding, we can sell at prices[i] and skip day i+1 (cooldown),
               or do nothing.
            3. If not holding, we can buy at prices[i] or do nothing.
            4. Memoize all states.

        Complexity:
            Time: O(n) where n is the number of prices
            Space: O(n) for memoization
        """

        @cache
        def dfs(day: int, is_holding: int) -> int:
            if day >= len(prices):
                return 0
            profit = dfs(day + 1, is_holding)
            if is_holding:
                profit = max(profit, prices[day] + dfs(day + 2, 0))
            else:
                profit = max(profit, -prices[day] + dfs(day + 1, 1))
            return profit

        return dfs(0, 0)
