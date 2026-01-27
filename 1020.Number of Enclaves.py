from itertools import pairwise


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        """Number of Enclaves via boundary DFS flood fill.

        Intuition:
            Land cells connected to the border cannot be enclaves. Flood-fill
            from all border land cells to mark them, then count remaining land.

        Approach:
            Use DFS from every border cell that is land, setting visited cells
            to 0. After processing all borders, sum the remaining 1s in the grid.

        Complexity:
            Time: O(m * n)
            Space: O(m * n) for recursion stack in worst case
        """

        def dfs(row: int, col: int) -> None:
            grid[row][col] = 0
            for delta_r, delta_c in pairwise(directions):
                next_row, next_col = row + delta_r, col + delta_c
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col]
                ):
                    dfs(next_row, next_col)

        rows, cols = len(grid), len(grid[0])
        directions = (-1, 0, 1, 0, -1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                    dfs(i, j)
        return sum(cell for row in grid for cell in row)
