from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """Bitmask game theory with memoized DFS.

        Intuition:
            Each state of the game is defined by which numbers have been
            chosen, representable as a bitmask. A player wins if they can
            reach the target or force the opponent into a losing state.

        Approach:
            Use a bitmask to track chosen numbers. Recursively try each
            unchosen number: if choosing it reaches the target or puts the
            opponent in a losing position, the current player wins. Memoize
            on the bitmask and running sum.

        Complexity:
            Time: O(2^n * n) where n = maxChoosableInteger
            Space: O(2^n)
        """

        @cache
        def dfs(mask: int, current_sum: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                if mask >> i & 1 ^ 1:
                    if current_sum + i >= desiredTotal or not dfs(
                        mask | 1 << i, current_sum + i
                    ):
                        return True
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0, 0)
