class Solution:
    def minimizeError(self, prices: list[str], target: int) -> str:
        """Minimize total rounding error when rounding prices to meet target.

        Intuition:
            Each fractional price can be rounded up or down. Greedily round up
            the prices with the largest fractional parts to minimize total error.

        Approach:
            Compute floor sum and collect fractional parts. Sort fractions
            descending, round up the top `d` values where d = target - floor_sum.

        Complexity:
            Time: O(n log n) for sorting fractional parts
            Space: O(n) for the fractions array
        """
        floor_sum = 0
        fractions = []
        for price_str in prices:
            price = float(price_str)
            floor_sum += int(price)
            if fractional := price - int(price):
                fractions.append(fractional)
        if not floor_sum <= target <= floor_sum + len(fractions):
            return "-1"
        round_up_count = target - floor_sum
        fractions.sort(reverse=True)
        total_error = (
            round_up_count
            - sum(fractions[:round_up_count])
            + sum(fractions[round_up_count:])
        )
        return f"{total_error:.3f}"
