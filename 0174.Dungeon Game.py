from math import inf


class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        """Bottom-right to top-left DP computing minimum initial health.

        Intuition:
            Working backwards from the princess's cell, we can determine the
            minimum health needed at each cell to survive the path. The knight
            must always have at least 1 HP.

        Approach:
            1. Create a DP table of size (m+1) x (n+1) initialized to infinity.
            2. Set boundary conditions: dp[m][n-1] = dp[m-1][n] = 1.
            3. Fill DP from bottom-right to top-left: dp[i][j] = max(1, min of
               right/down neighbors minus current dungeon value).

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[inf] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]
