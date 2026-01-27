from itertools import pairwise


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """DFS Flood Fill Approach

        Intuition:
            Treat each '1' cell as part of an island. Use DFS to mark
            all connected land cells as visited, counting each new DFS
            initiation as a separate island.

        Approach:
            1. Iterate through every cell in the grid.
            2. When a '1' is found, increment the island count and run DFS.
            3. DFS marks the current cell as '0' and recurses on all
               4-directional neighbors that are '1'.

        Complexity:
            Time: O(m * n) where m and n are grid dimensions
            Space: O(m * n) for recursion stack in worst case
        """

        def dfs(row: int, col: int) -> None:
            grid[row][col] = "0"
            for delta_r, delta_c in pairwise(directions):
                next_row, next_col = row + delta_r, col + delta_c
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == "1"
                ):
                    dfs(next_row, next_col)

        island_count = 0
        directions = (-1, 0, 1, 0, -1)
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island_count += 1
        return island_count
