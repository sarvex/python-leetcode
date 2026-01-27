class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """Shift all elements of a 2D grid k positions to the right.

        Intuition:
            Flattening the grid conceptually, each element at linear index idx
            moves to (idx + k) mod total_elements. Convert back to 2D coords.

        Approach:
            For each cell (i, j), compute its new position after shifting by k
            in the flattened representation using modular arithmetic and divmod.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(grid), len(grid[0])
        total = rows * cols
        result = [[0] * cols for _ in range(rows)]
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                new_row, new_col = divmod((i * cols + j + k) % total, cols)
                result[new_row][new_col] = value
        return result
