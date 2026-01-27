class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        """Row-by-row DP taking minimum from adjacent columns above.

        Intuition:
            For each cell, the minimum falling path sum is the cell value
            plus the minimum of the three adjacent cells in the previous row.

        Approach:
            1. Initialize a DP array of zeros.
            2. For each row, compute the new DP values considering the
               minimum of adjacent columns from the previous row.
            3. Return the minimum value in the final DP array.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        size = len(matrix)
        prev_row = [0] * size
        for row in matrix:
            curr_row = [0] * size
            for col, value in enumerate(row):
                left_bound = max(0, col - 1)
                right_bound = min(size, col + 2)
                curr_row[col] = min(prev_row[left_bound:right_bound]) + value
            prev_row = curr_row
        return min(prev_row)
