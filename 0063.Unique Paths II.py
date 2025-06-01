from typing import List
from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """Dynamic Programming with Memoization

Intuition:
Robot can only move right or down, so paths to a cell equal sum of paths from above and left.
Obstacles block paths, making those cells unreachable (0 paths).

Approach:
Use top-down DP with memoization to avoid recalculating paths.
Recursively calculate paths from start to each cell, caching results.

Complexity:
Time: O(m*n) where m and n are the dimensions of the grid
Space: O(m*n) for the memoization cache
"""
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Early return if start or end has obstacle
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        @cache
        def dfs(i: int, j: int) -> int:
            # Out of bounds or obstacle
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0

            # Return 1 if destination reached, otherwise explore further
            return 1 if i == m - 1 and j == n - 1 else dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
