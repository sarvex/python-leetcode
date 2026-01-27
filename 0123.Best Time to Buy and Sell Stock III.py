class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """State Machine Dynamic Programming Approach

        Intuition:
            With at most two transactions, we track four states: after first buy,
            after first sell, after second buy, and after second sell. Each state
            transitions optimally from the previous one.

        Approach:
            Initialize four state variables representing the maximum profit at each
            stage. Iterate through prices updating each state greedily: first buy
            minimizes cost, first sell maximizes profit from first buy, second buy
            maximizes profit minus cost after first sell, second sell maximizes
            total profit.

        Complexity:
            Time: O(n) where n is the number of prices
            Space: O(1)
        """
        first_buy, first_sell, second_buy, second_sell = -prices[0], 0, -prices[0], 0
        for price in prices[1:]:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        return second_sell
