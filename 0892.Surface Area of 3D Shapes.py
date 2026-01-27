class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        """Grid traversal subtracting shared faces between adjacent columns.

        Intuition:
            Each column of height v contributes 2 (top+bottom) + 4*v (sides).
            Shared faces between adjacent columns reduce the surface area.

        Approach:
            1. For each non-zero cell, add 2 + 4 * height.
            2. Subtract 2 * min(height, neighbor_height) for each adjacent
               cell above and to the left to remove hidden faces.

        Complexity:
            Time: O(n * m)
            Space: O(1)
        """
        total_area = 0
        for row_index, row in enumerate(grid):
            for col_index, height in enumerate(row):
                if height:
                    total_area += 2 + height * 4
                    if row_index:
                        total_area -= min(height, grid[row_index - 1][col_index]) * 2
                    if col_index:
                        total_area -= min(height, grid[row_index][col_index - 1]) * 2
        return total_area
