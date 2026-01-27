from itertools import pairwise


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        """Count islands of 0s completely surrounded by 1s using DFS.

        Intuition:
            A closed island is a connected component of 0s that does not touch
            the boundary. We can use DFS to explore each component and check
            whether all cells are interior (not on the grid boundary).

        Approach:
            For each unvisited land cell (0), run DFS marking cells as visited
            (setting to 1). The DFS returns whether all cells in the component
            are strictly interior. Count components where all cells are interior.

        Complexity:
            Time: O(m * n) — each cell visited at most once
            Space: O(m * n) — recursion stack in worst case
        """

        def dfs(row: int, col: int) -> int:
            is_closed = int(0 < row < num_rows - 1 and 0 < col < num_cols - 1)
            grid[row][col] = 1
            for delta_r, delta_c in pairwise(directions):
                next_row, next_col = row + delta_r, col + delta_c
                if (
                    0 <= next_row < num_rows
                    and 0 <= next_col < num_cols
                    and grid[next_row][next_col] == 0
                ):
                    is_closed &= dfs(next_row, next_col)
            return is_closed

        num_rows, num_cols = len(grid), len(grid[0])
        directions = (-1, 0, 1, 0, -1)
        return sum(
            grid[i][j] == 0 and dfs(i, j)
            for i in range(num_rows)
            for j in range(num_cols)
        )
