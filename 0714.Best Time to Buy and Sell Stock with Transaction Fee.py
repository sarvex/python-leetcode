from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """DP with state machine approach

        Intuition:
        We can represent our position in the market with two states:
        - Not holding a stock (can buy)
        - Holding a stock (can sell)

        Approach:
        Use dynamic programming with memoization to explore all possible buy/sell
        decisions at each day. The state is defined by (day, holding) where:
        - day: current day index
        - holding: 1 if holding stock, 0 if not holding

        Complexity:
        Time: O(n) where n is the length of prices array
        Space: O(n) for the memoization cache
        """
        @cache
        def dfs(day: int, holding: int) -> int:
            # Base case: reached the end of the timeline
            if day >= len(prices):
                return 0

            # Option 1: Skip this day (do nothing)
            max_profit = dfs(day + 1, holding)

            if holding:
                # Option 2: Sell the stock we're holding
                # Get price, subtract fee, and transition to not holding
                max_profit = max(max_profit, prices[day] - fee + dfs(day + 1, 0))
            else:
                # Option 2: Buy a stock
                # Pay the price and transition to holding
                max_profit = max(max_profit, -prices[day] + dfs(day + 1, 1))

            return max_profit

        # Start on day 0, not holding any stock
        return dfs(0, 0)
