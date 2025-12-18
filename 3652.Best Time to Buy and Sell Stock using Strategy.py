from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Calculate the base profit with the original strategy
        base_profit = 0
        for p, s in zip(prices, strategy):
            base_profit += p * s

        # Initial window calculation (indices 0 to k-1)
        half_k = k // 2

        # Contribution of the original strategy in the first window
        current_window_original_profit = 0
        for i in range(k):
            current_window_original_profit += strategy[i] * prices[i]

        # Contribution of the modified strategy in the first window
        # The modified strategy sets the first k/2 to 0 (hold) and last k/2 to 1 (sell).
        # So only the second half prices contribute.
        current_window_modified_profit = 0
        for i in range(half_k, k):
            current_window_modified_profit += prices[i]

        max_profit_diff = (
            current_window_modified_profit - current_window_original_profit
        )

        # Slide the window
        # Loop runs for the transitions. i represents the index that is being removed from the start of the window.
        for i in range(n - k):
            # Window moves from [i, i+k-1] to [i+1, i+k]

            # --- Update original strategy profit in the window ---
            # Remove strategy[i]*prices[i], Add strategy[i+k]*prices[i+k]
            current_window_original_profit -= strategy[i] * prices[i]
            current_window_original_profit += strategy[i + k] * prices[i + k]

            # --- Update modified strategy profit in the window ---
            # Previous Sell Range: [i + half_k, i + k - 1]
            # New Sell Range:      [i + 1 + half_k, i + k]
            # We remove prices[i + half_k] and add prices[i+k]
            current_window_modified_profit -= prices[i + half_k]
            current_window_modified_profit += prices[i + k]

            diff = current_window_modified_profit - current_window_original_profit
            if diff > max_profit_diff:
                max_profit_diff = diff

        return base_profit + max(0, max_profit_diff)
