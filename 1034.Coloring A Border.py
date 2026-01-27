from itertools import pairwise


class Solution:
    def colorBorder(
        self, grid: list[list[int]], row: int, col: int, color: int
    ) -> list[list[int]]:
        """Coloring A Border using DFS to identify border cells.

        Intuition:
            A cell is a border cell of its connected component if it is on
            the grid boundary or adjacent to a cell of a different color.

        Approach:
            DFS from the starting cell, marking visited cells. For each cell,
            check all neighbors: if a neighbor is out of bounds or a different
            color, the current cell is a border and gets recolored.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """

        def dfs(i: int, j: int, original: int) -> None:
            visited[i][j] = True
            for delta_r, delta_c in pairwise((-1, 0, 1, 0, -1)):
                next_row, next_col = i + delta_r, j + delta_c
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if not visited[next_row][next_col]:
                        if grid[next_row][next_col] == original:
                            dfs(next_row, next_col, original)
                        else:
                            grid[i][j] = color
                else:
                    grid[i][j] = color

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dfs(row, col, grid[row][col])
        return grid
