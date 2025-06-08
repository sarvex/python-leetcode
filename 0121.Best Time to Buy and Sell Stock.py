from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """One-pass solution using minimum price tracking.

        Intuition:
            To maximize profit, we need to buy at the lowest price and sell at the highest
            price after buying. We can track the minimum price seen so far and calculate
            the potential profit at each step.

        Approach:
            Iterate through the prices once, keeping track of:
            1. The minimum price seen so far
            2. The maximum profit possible by selling at the current price

        Complexity:
            Time: O(n) where n is the length of the prices array
            Space: O(1) constant extra space
        """
        profit = 0
        minimum = float('inf')

        for price in prices:
            # Try to sell at current price and update max profit if better
            profit = max(profit, price - minimum)
            # Update minimum price seen so far
            minimum = min(minimum, price)

        return profit
