class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """Dynamic programming to find the largest square of ones.

        Intuition:
            Each cell stores the side length of the largest square ending at that
            cell. It depends on the minimum of its top, left, and top-left neighbors.

        Approach:
            1. Create a DP table with an extra row and column (zero-indexed offset).
            2. For each '1' cell, dp[i+1][j+1] = min(top, left, diagonal) + 1.
            3. Track the maximum side length seen.
            4. Return the area (max_side^2).

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    dp[row + 1][col + 1] = (
                        min(dp[row][col + 1], dp[row + 1][col], dp[row][col]) + 1
                    )
                    max_side = max(max_side, dp[row + 1][col + 1])
        return max_side * max_side
