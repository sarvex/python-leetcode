class Solution:
    def oddCells(self, rows: int, cols: int, indices: list[list[int]]) -> int:
        """Count cells with odd values after applying row/column increments.

        Intuition:
            Each index operation increments an entire row and an entire column.
            We can simulate the process by building the full grid and counting
            odd-valued cells at the end.

        Approach:
            Initialize an m x n grid of zeros. For each (row, col) in indices,
            increment all cells in the specified column and all cells in the
            specified row. Finally count cells with odd values.

        Complexity:
            Time: O(len(indices) * (m + n) + m * n) — increments plus counting
            Space: O(m * n) — for the grid
        """
        grid = [[0] * cols for _ in range(rows)]
        for row_idx, col_idx in indices:
            for i in range(rows):
                grid[i][col_idx] += 1
            for j in range(cols):
                grid[row_idx][j] += 1
        return sum(value % 2 for row in grid for value in row)
