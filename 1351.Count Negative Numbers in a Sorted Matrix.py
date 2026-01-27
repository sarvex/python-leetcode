class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """Count negative numbers in a sorted matrix.

        Intuition:
            Since rows and columns are sorted in non-increasing order, we can
            exploit the staircase boundary between non-negative and negative
            values by starting from the bottom-left corner.

        Approach:
            Start at bottom-left. If the current cell is negative, all cells to
            its right are also negative so add them and move up. Otherwise move
            right. This traces the boundary in O(m + n) time.

        Complexity:
            Time: O(m + n) where m is rows and n is columns.
            Space: O(1)
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        count = 0

        row, col = num_rows - 1, 0

        while row >= 0 and col < num_cols:
            if grid[row][col] < 0:
                count += num_cols - col
                row -= 1
            else:
                col += 1

        return count
