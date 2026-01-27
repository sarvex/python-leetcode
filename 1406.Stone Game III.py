from functools import cache
from math import inf


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        """Determine the winner of stone game with optimal play.

        Intuition:
            Use minimax: each player maximizes their own score minus the
            opponent's future score by taking 1, 2, or 3 stones.

        Approach:
            Define a recursive function with memoization. At each position,
            try taking 1-3 stones and compute score minus opponent's best.
            Positive result means Alice wins, negative means Bob, zero is tie.

        Complexity:
            Time: O(n) with memoization (3 choices per state)
            Space: O(n) for the cache
        """

        @cache
        def max_score_diff(index: int) -> int:
            if index >= length:
                return 0
            best, taken = -inf, 0
            for take in range(3):
                if index + take >= length:
                    break
                taken += stoneValue[index + take]
                best = max(best, taken - max_score_diff(index + take + 1))
            return best

        length = len(stoneValue)
        result = max_score_diff(0)
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"
