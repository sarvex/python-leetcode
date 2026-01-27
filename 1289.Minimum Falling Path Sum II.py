class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        """Minimum falling path sum in a grid with no two adjacent-row same-column constraint.

        Intuition:
            For each cell, the minimum falling path must come from a different column
            in the previous row.

        Approach:
            Use DP where dp[i][j] is the minimum path sum ending at row i, column j.
            For each cell, take the minimum of all dp values in the previous row
            excluding the same column.

        Complexity:
            Time: O(n^3)
            Space: O(n^2)
        """
        size = len(grid)
        dp = [[0] * size for _ in range(size + 1)]
        for i, row in enumerate(grid, 1):
            for j, value in enumerate(row):
                min_prev = min((dp[i - 1][k] for k in range(size) if k != j), default=0)
                dp[i][j] = value + min_prev
        return min(dp[size])
