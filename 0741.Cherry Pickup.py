from math import inf


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        """3D DP simulating two simultaneous paths for maximum cherry collection.

        Intuition:
            Instead of going down-right then up-left, model two people walking
            down-right simultaneously. At each step k, both have moved k cells
            from the origin.

        Approach:
            1. Let dp[k][i1][i2] be the max cherries when person 1 is at row i1
               and person 2 is at row i2, both having taken k steps.
            2. Transition from the four combinations of previous rows (i1-1, i1)
               and (i2-1, i2).
            3. Add cherries from both positions, avoiding double-counting.

        Complexity:
            Time: O(N^3)
            Space: O(N^3)
        """
        size = len(grid)
        dp = [[[-inf] * size for _ in range(size)] for _ in range((size << 1) - 1)]
        dp[0][0][0] = grid[0][0]
        for step in range(1, (size << 1) - 1):
            for row1 in range(size):
                for row2 in range(size):
                    col1, col2 = step - row1, step - row2
                    if (
                        not 0 <= col1 < size
                        or not 0 <= col2 < size
                        or grid[row1][col1] == -1
                        or grid[row2][col2] == -1
                    ):
                        continue
                    cherries = grid[row1][col1]
                    if row1 != row2:
                        cherries += grid[row2][col2]
                    for prev_row1 in range(row1 - 1, row1 + 1):
                        for prev_row2 in range(row2 - 1, row2 + 1):
                            if prev_row1 >= 0 and prev_row2 >= 0:
                                dp[step][row1][row2] = max(
                                    dp[step][row1][row2],
                                    dp[step - 1][prev_row1][prev_row2] + cherries,
                                )
        return max(0, dp[-1][-1][-1])
