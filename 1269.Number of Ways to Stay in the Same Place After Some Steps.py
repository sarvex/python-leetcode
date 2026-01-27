from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """Count ways to return to index 0 after exactly steps moves.

        Intuition:
            At each step we can move left, right, or stay. We need to count
            paths that end at position 0 after all steps. Memoization on
            (position, remaining_steps) avoids redundant computation.

        Approach:
            Use top-down DP with memoization. State is (position, remaining
            steps). Base case: position 0 with 0 steps remaining returns 1.
            Invalid states (out of bounds or negative steps) return 0.

        Complexity:
            Time: O(steps * min(steps, arrLen))
            Space: O(steps * min(steps, arrLen))
        """

        @cache
        def dfs(position: int, remaining: int) -> int:
            if (
                position > remaining
                or position >= arrLen
                or position < 0
                or remaining < 0
            ):
                return 0
            if position == 0 and remaining == 0:
                return 1
            total = 0
            for delta in range(-1, 2):
                total += dfs(position + delta, remaining - 1)
                total %= MOD
            return total

        MOD = 10**9 + 7
        return dfs(0, steps)
