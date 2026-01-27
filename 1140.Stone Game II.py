from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """Return the maximum stones Alice can collect in Stone Game II.

        Intuition:
            Both players play optimally, so we can model the game with
            minimax. The current player maximizes their gain, which equals
            the remaining total minus the opponent's optimal gain.

        Approach:
            Use memoized DFS with prefix sums. At each state (index, M), the
            current player can take 1 to 2*M piles. The player's score is the
            remaining sum minus the opponent's optimal result from the next state.

        Complexity:
            Time: O(n^3) where n is the number of piles
            Space: O(n^2) for the memoization cache
        """
        num_piles = len(piles)
        prefix_sum = list(accumulate(piles, initial=0))

        @cache
        def dfs(index: int, max_take: int) -> int:
            if max_take * 2 >= num_piles - index:
                return prefix_sum[num_piles] - prefix_sum[index]
            return max(
                prefix_sum[num_piles]
                - prefix_sum[index]
                - dfs(index + take, max(max_take, take))
                for take in range(1, max_take * 2 + 1)
            )

        return dfs(0, 1)
