class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Row-Column Marker Approach

        Intuition:
            First identify which rows and columns contain zeros, then
            set the entire row/column to zero in a second pass.

        Approach:
            Use two boolean arrays to record which rows and columns
            contain at least one zero. Then iterate through the matrix
            again and set any cell to zero if its row or column is marked.

        Complexity:
            Time: O(m * n)
            Space: O(m + n)
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        zero_rows = [0] * num_rows
        zero_cols = [0] * num_cols
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    zero_rows[i] = zero_cols[j] = 1
        for i in range(num_rows):
            for j in range(num_cols):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0
