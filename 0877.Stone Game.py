from functools import cache


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        """Minimax with memoization computing optimal score difference.

        Intuition:
            Each player picks optimally from either end. Track the score
            difference using recursion: positive means current player leads.

        Approach:
            1. Define a recursive function that returns the net score advantage
               for the current player over the subarray [left, right].
            2. At each step, the current player picks the left or right pile,
               and the opponent plays optimally on the remaining subarray.
            3. Memoize to avoid recomputation.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """

        @cache
        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            return max(
                piles[left] - dfs(left + 1, right), piles[right] - dfs(left, right - 1)
            )

        return dfs(0, len(piles) - 1) > 0
