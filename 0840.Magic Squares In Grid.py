class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        """Check all 3x3 subgrids for magic square properties.

        Intuition:
            A 3x3 magic square uses digits 1-9 exactly once with equal row,
            column, and diagonal sums. Check each possible subgrid.

        Approach:
            1. For each 3x3 subgrid, verify all values are 1-9 and distinct.
            2. Check that all rows, columns, and diagonals sum to the same value.

        Complexity:
            Time: O(m * n) where m, n are grid dimensions
            Space: O(1)
        """

        def is_magic_square(top_row: int, left_col: int) -> int:
            if top_row + 3 > rows or left_col + 3 > cols:
                return 0
            seen: set[int] = set()
            row_sums = [0] * 3
            col_sums = [0] * 3
            main_diag = anti_diag = 0
            for row in range(top_row, top_row + 3):
                for col in range(left_col, left_col + 3):
                    value = grid[row][col]
                    if value < 1 or value > 9:
                        return 0
                    seen.add(value)
                    row_sums[row - top_row] += value
                    col_sums[col - left_col] += value
                    if row - top_row == col - left_col:
                        main_diag += value
                    if row - top_row == 2 - (col - left_col):
                        anti_diag += value
            if len(seen) != 9 or main_diag != anti_diag:
                return 0
            if any(total != main_diag for total in row_sums) or any(
                total != main_diag for total in col_sums
            ):
                return 0
            return 1

        rows, cols = len(grid), len(grid[0])
        return sum(is_magic_square(i, j) for i in range(rows) for j in range(cols))
