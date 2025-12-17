from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # profit[t][i] stores the max profit using at most t transactions
        # considering prices up to day i.
        # Dimensions: (k+1) x n
        profit = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            # We want to find max profit for t transactions.
            # At each day i, we can potentially complete a transaction that started at j < i.
            # Normal transaction (Buy j, Sell i): Profit = prices[i] - prices[j]
            # Short transaction (Sell j, Buy i):  Profit = prices[j] - prices[i]
            # In both cases, we add the profit from t-1 transactions ending before j.

            # We maintain two running max values to avoid O(N) inner loop:
            # mx_minus = max(profit[t-1][j-1] - prices[j]) for valid j
            # mx_plus  = max(profit[t-1][j-1] + prices[j]) for valid j

            # Initial values for j=0.
            # profit[t-1][-1] is effectively 0.
            mx_minus = -prices[0]  # Equivalent to 0 - prices[0]
            mx_plus = prices[0]  # Equivalent to 0 + prices[0]

            for i in range(1, n):
                # Calculate potential profit if we end a transaction at day i
                # using the best start day j found so far (j < i).

                # Normal transaction: prices[i] + max(profit - prices[j])
                val_normal = mx_minus + prices[i]

                # Short transaction: -prices[i] + max(profit + prices[j])
                val_short = mx_plus - prices[i]

                # Best profit at day i is either:
                # 1. Carrying over profit from day i-1 (no transaction ends at i)
                # 2. Completing a transaction at i
                profit[t][i] = max(profit[t][i - 1], val_normal, val_short)

                # Update running max sets for the next iteration (where i becomes a candidate start day j).
                # If we start a new transaction at j=i, the previous transaction must have ended at <= i-1.
                prev_profit = profit[t - 1][i - 1]

                mx_minus = max(mx_minus, prev_profit - prices[i])
                mx_plus = max(mx_plus, prev_profit + prices[i])

        return profit[k][n - 1]
