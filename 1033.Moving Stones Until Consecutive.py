class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        """Moving Stones Until Consecutive with min/max move analysis.

        Intuition:
            The maximum moves equal the total gaps minus 2. The minimum moves
            depend on whether stones are already consecutive or near-consecutive.

        Approach:
            Sort the three values. Maximum moves fill every empty slot between
            min and max. Minimum moves: 0 if consecutive, 1 if any pair has a
            gap of 2 or less, otherwise 2.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        low, high = min(a, b, c), max(a, b, c)
        mid = a + b + c - low - high
        min_moves = max_moves = 0
        if high - low > 2:
            min_moves = 1 if mid - low < 3 or high - mid < 3 else 2
            max_moves = high - low - 2
        return [min_moves, max_moves]
