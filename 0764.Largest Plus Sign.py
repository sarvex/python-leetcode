class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        """DP tracking arm lengths in four directions for each cell.

        Intuition:
            The order of a plus sign at a cell is the minimum arm length in
            all four directions. Compute each direction in a single pass.

        Approach:
            1. Initialize a grid with value n (maximum possible arm).
            2. Set mined cells to 0.
            3. For each row/column, sweep in both directions to compute
               consecutive non-zero counts, taking the minimum with the
               current cell value.

        Complexity:
            Time: O(N^2)
            Space: O(N^2)
        """
        dp = [[n] * n for _ in range(n)]
        for row, col in mines:
            dp[row][col] = 0
        for i in range(n):
            left = right = up = down = 0
            for j, k in zip(range(n), reversed(range(n))):
                left = left + 1 if dp[i][j] else 0
                right = right + 1 if dp[i][k] else 0
                up = up + 1 if dp[j][i] else 0
                down = down + 1 if dp[k][i] else 0
                dp[i][j] = min(dp[i][j], left)
                dp[i][k] = min(dp[i][k], right)
                dp[j][i] = min(dp[j][i], up)
                dp[k][i] = min(dp[k][i], down)
        return max(max(row) for row in dp)
