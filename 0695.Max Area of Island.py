from itertools import pairwise


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """DFS flood fill to compute the maximum island area.

        Intuition:
            Each connected component of 1s forms an island. Use DFS to explore
            each island, counting cells, and track the maximum area found.

        Approach:
            1. Iterate over all cells. For each unvisited land cell, run DFS.
            2. Mark visited cells by setting them to 0.
            3. Count the size of each island and return the maximum.

        Complexity:
            Time: O(m * n) visiting each cell at most once
            Space: O(m * n) worst case recursion depth
        """

        def dfs(row: int, col: int) -> int:
            if grid[row][col] == 0:
                return 0
            area = 1
            grid[row][col] = 0
            directions = (-1, 0, 1, 0, -1)
            for delta_row, delta_col in pairwise(directions):
                next_row, next_col = row + delta_row, col + delta_col
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    area += dfs(next_row, next_col)
            return area

        rows, cols = len(grid), len(grid[0])
        return max(dfs(i, j) for i in range(rows) for j in range(cols))
