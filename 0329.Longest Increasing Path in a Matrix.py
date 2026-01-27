from functools import cache
from itertools import pairwise


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """DFS with memoization for longest increasing path.

        Intuition:
            From each cell, explore all four neighbors with strictly greater
            values. Memoize results to avoid redundant computation.

        Approach:
            1. For each cell, recursively compute the longest increasing path
               starting from that cell using cached DFS.
            2. Return the maximum across all cells.

        Complexity:
            Time: O(m * n) where m and n are matrix dimensions
            Space: O(m * n) for the memoization cache
        """

        @cache
        def dfs(row: int, col: int) -> int:
            best = 0
            for delta_r, delta_c in pairwise((-1, 0, 1, 0, -1)):
                next_row, next_col = row + delta_r, col + delta_c
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and matrix[next_row][next_col] > matrix[row][col]
                ):
                    best = max(best, dfs(next_row, next_col))
            return best + 1

        rows, cols = len(matrix), len(matrix[0])
        return max(dfs(i, j) for i in range(rows) for j in range(cols))
