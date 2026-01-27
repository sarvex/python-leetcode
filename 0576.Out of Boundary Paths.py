from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        """Count paths that move the ball out of the grid boundary using DFS with memoization.

        Intuition:
            From any cell, the ball can move in four directions. If it crosses
            the boundary, that counts as one valid path. We recursively explore
            all directions with remaining moves and cache results.

        Approach:
            1. Use depth-first search with memoization on (row, col, remaining_moves).
            2. Base case: if out of bounds, return 1 (found a valid path).
            3. Base case: if no moves remaining, return 0.
            4. Sum up results from all four directions, taking modulo at each step.

        Complexity:
            Time: O(m * n * maxMove)
            Space: O(m * n * maxMove)
        """
        mod = 10**9 + 7

        @cache
        def dfs(row: int, col: int, remaining: int) -> int:
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if remaining <= 0:
                return 0
            result = 0
            for delta_row, delta_col in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                next_row, next_col = row + delta_row, col + delta_col
                result += dfs(next_row, next_col, remaining - 1)
                result %= mod
            return result

        return dfs(startRow, startColumn, maxMove)
