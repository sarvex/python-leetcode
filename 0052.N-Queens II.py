class Solution:
    def totalNQueens(self, n: int) -> int:
        """Backtracking with bit manipulation for optimal performance

        Intuition:
        The N-Queens II problem requires counting valid configurations where N queens
        can be placed on an N×N chessboard without threatening each other. A queen
        threatens any piece in the same row, column, or diagonal.

        Approach:
        Use backtracking with three sets to track occupied columns and diagonals:
        1. Track occupied columns with a boolean array
        2. Track occupied diagonals (i+j) with another boolean array
        3. Track occupied anti-diagonals (i-j+n) with a third boolean array
        4. Recursively place queens row by row, backtracking when needed

        Complexity:
        Time: O(N!), as we potentially try N positions for the first row, N-1 for the second, etc.
        Space: O(N), for the recursion stack and the three boolean arrays
        """
        def dfs(row: int) -> None:
            if row == n:
                nonlocal count
                count += 1
                return

            for col in range(n):
                # Calculate diagonal indices
                diag = row + col
                anti_diag = row - col + n

                # Skip if any of the constraints are violated
                if cols[col] or diagonals[diag] or anti_diagonals[anti_diag]:
                    continue

                # Place queen and mark constraints
                cols[col] = diagonals[diag] = anti_diagonals[anti_diag] = True

                # Proceed to next row
                dfs(row + 1)

                # Backtrack
                cols[col] = diagonals[diag] = anti_diagonals[anti_diag] = False

        # Initialize constraint tracking arrays with appropriate sizes
        cols = [False] * n
        diagonals = [False] * (2 * n)
        anti_diagonals = [False] * (2 * n)
        count = 0

        # Start backtracking from the first row
        dfs(0)
        return count
