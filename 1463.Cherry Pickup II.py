from itertools import product


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        """Maximize cherries collected by two robots traversing a grid.

        Intuition:
            Both robots move downward simultaneously; use 3D DP tracking
            row and both column positions.

        Approach:
            DP where dp[row][col1][col2] stores the maximum cherries collected
            when robot 1 is at col1 and robot 2 is at col2 on the given row.
            For each row, try all 9 combinations of movements (-1, 0, +1) for
            both robots from the previous row.

        Complexity:
            Time: O(m * n^2 * 9) where m is rows and n is columns
            Space: O(m * n^2)
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]

        for row in range(1, rows):
            for col1 in range(cols):
                for col2 in range(cols):
                    cherries = grid[row][col1] + (
                        0 if col1 == col2 else grid[row][col2]
                    )
                    for prev_col1 in range(col1 - 1, col1 + 2):
                        for prev_col2 in range(col2 - 1, col2 + 2):
                            if (
                                0 <= prev_col1 < cols
                                and 0 <= prev_col2 < cols
                                and dp[row - 1][prev_col1][prev_col2] != -1
                            ):
                                dp[row][col1][col2] = max(
                                    dp[row][col1][col2],
                                    dp[row - 1][prev_col1][prev_col2] + cherries,
                                )

        return max(
            dp[-1][col1][col2] for col1, col2 in product(range(cols), range(cols))
        )
