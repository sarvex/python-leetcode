from itertools import pairwise


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """3D DP tracking knight probability after k moves on an n×n board.

        Intuition:
            Use dynamic programming where dp[step][i][j] represents the
            probability of being at cell (i, j) after exactly 'step' moves,
            starting from probability 1.0 at every cell for step 0.

        Approach:
            1. Initialize dp[0][i][j] = 1 for all cells.
            2. For each subsequent step, accumulate probabilities from all 8
               valid knight-move predecessors, each contributing 1/8.
            3. Return dp[k][row][column].

        Complexity:
            Time: O(k * n^2) iterating over all cells for each step
            Space: O(k * n^2) for the 3D DP table
        """
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1
        for step in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for delta_row, delta_col in pairwise(
                        (-2, -1, 2, 1, -2, 1, 2, -1, -2)
                    ):
                        prev_row, prev_col = i + delta_row, j + delta_col
                        if 0 <= prev_row < n and 0 <= prev_col < n:
                            dp[step][i][j] += dp[step - 1][prev_row][prev_col] / 8
        return dp[k][row][column]
