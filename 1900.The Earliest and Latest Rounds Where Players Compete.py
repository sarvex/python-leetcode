from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """
        Calculates the earliest and latest rounds where two players can compete.

        This solution uses a top-down dynamic programming approach with memoization
        to explore all possible outcomes of the tournament.

        Intuition:
        The problem requires finding the min and max rounds until two players meet.
        Since match winners are random, we must explore all valid tournament progressions.
        A recursive approach with memoization is suitable. The state of the recursion
        can be defined by the number of players left in the tournament (`k`) and the
        1-indexed positions of our two players (`i` and `j`) within that group.

        Approach:
        We define a recursive function `dp(k, i, j)`:
        1.  **State**: `k` = total players, `i` = position of first player, `j` = position of second player.
        2.  **Base Case**: If `i + j == k + 1`, the players meet in this round. Return `[1, 1]`.
        3.  **Recursive Step**: Iterate through all possible numbers of winners from the three
            groups of players: `i-1` players to the left of player `i`, `j-i-1` players
            between `i` and `j`, and `k-j` players to the right of player `j`.
            - Let `x` be the number of winners from the left group.
            - Let `y` be the number of winners from the between group.
            The number of winners from the right group is determined by the total players
            advancing to the next round: `(k+1)//2`.
            For each valid combination of `x` and `y`, calculate the new positions of our
            players (`i_new = x + 1`, `j_new = x + y + 2`) and recurse.
        4.  **Memoization**: Use `@lru_cache` on `dp(k, i, j)` to store results.

        The final result is `dp(n, firstPlayer, secondPlayer)`.

        Complexity:
        - Time: O(n^4) - The state is O(n^3), and each transition takes O(n^2).
        - Space: O(n^3) - For the memoization cache.
        """
        @lru_cache(None)
        def dp(k, i, j):
            if i > j:
                return dp(k, j, i)

            if i + j == k + 1:
                return [1, 1]

            res = [inf, -inf]
            m = (k + 1) // 2

            for x in range(i):
                for y in range(j - i):
                    if m - 2 - x - y < 0 or m - 2 - x - y > k - j:
                        continue

                    i_new, j_new = x + 1, x + y + 2
                    sub_res = dp(m, i_new, j_new)
                    res[0] = min(res[0], sub_res[0] + 1)
                    res[1] = max(res[1], sub_res[1] + 1)

            return res

        return dp(n, firstPlayer, secondPlayer)
