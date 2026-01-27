import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """Mathematical formula using the quadratic solution for staircase rows.

        Intuition:
            k complete rows use k*(k+1)/2 coins. Solving k*(k+1)/2 <= n gives
            k = floor(sqrt(2*n + 0.25) - 0.5).

        Approach:
            1. Apply the closed-form solution derived from the quadratic formula.
            2. Return the integer result.

        Complexity:
            Time: O(1) for the mathematical computation.
            Space: O(1) with no extra storage.
        """
        return int(math.sqrt(2) * math.sqrt(n + 0.125) - 0.5)
