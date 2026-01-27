class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        """Greedy row and column flipping to maximize binary row values.

        Intuition:
        The most significant bit contributes the most value. Ensure all rows
        start with 1 by flipping rows, then for each column maximize the
        count of 1s by optionally flipping columns.

        Approach:
        1. Flip any row whose first element is 0
        2. For each column, count 1s and take max(count, rows - count)
        3. Multiply each column's contribution by its positional power of 2

        Complexity:
        Time: O(m * n) where m is rows and n is columns
        Space: O(1) extra space (modifies grid in place)
        """
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            if grid[row][0] == 0:
                for col in range(cols):
                    grid[row][col] ^= 1
        total_score = 0
        for col in range(cols):
            ones_count = sum(grid[row][col] for row in range(rows))
            total_score += max(ones_count, rows - ones_count) * (1 << (cols - col - 1))
        return total_score
