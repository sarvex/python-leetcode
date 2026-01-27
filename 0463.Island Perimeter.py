class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """Count cell edges minus shared neighbor edges.

        Intuition:
            Each land cell contributes 4 edges, but shared edges between
            adjacent land cells must be subtracted.

        Approach:
            Iterate through each cell. For every land cell, add 4 to the
            perimeter. Subtract 2 for each adjacent land cell to the right
            or below (to avoid double-counting).

        Complexity:
            Time: O(m * n)
            Space: O(1)
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        perimeter -= 2
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        perimeter -= 2
        return perimeter
