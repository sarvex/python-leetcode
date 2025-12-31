from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Calculates the number of negative numbers in an m x n matrix grid
        which is sorted in non-increasing order both row-wise and column-wise.

        Time Complexity: O(m + n) where m is number of rows and n is number of columns.
        Space Complexity: O(1).
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        count = 0

        # Start from the bottom-left corner
        row, col = num_rows - 1, 0

        while row >= 0 and col < num_cols:
            if grid[row][col] < 0:
                # If grid[row][col] is negative, all elements to its right in the same row are negative
                count += num_cols - col
                # Move to the row above
                row -= 1
            else:
                # If grid[row][col] is non-negative, move to the next column
                col += 1

        return count
