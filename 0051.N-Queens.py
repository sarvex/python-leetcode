from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """N-Queens problem solver using backtracking with bit manipulation

        Intuition:
        Use backtracking to place queens row by row, ensuring no queen can attack another.
        Track occupied columns and diagonals to efficiently check valid positions.

        Approach:
        1. Use three arrays to track occupied columns and diagonals:
           - columns: tracks which columns have queens
           - diagonal: tracks occupied diagonals (i+j)
           - anti_diagonal: tracks occupied anti-diagonals (n-i+j)
        2. Place queens row by row using backtracking
        3. When all queens are placed (reached row n), add the board configuration to results

        Complexity:
        Time: O(N!), as we're exploring valid permutations of queen placements
        Space: O(N), for the recursion stack and tracking arrays
        """
        def backtrack(row: int) -> None:
            if row == n:
                # Found a valid configuration, add to results
                result.append(["".join(board_row) for board_row in board])
                return

            for col in range(n):
                # Check if placing a queen at position (row, col) is valid
                if columns[col] + diagonals[row + col] + anti_diagonals[n - row + col] == 0:
                    # Place queen
                    board[row][col] = "Q"
                    # Mark the column and diagonals as occupied
                    columns[col] = diagonals[row + col] = anti_diagonals[n - row + col] = 1

                    # Move to next row
                    backtrack(row + 1)

                    # Backtrack: remove queen and unmark
                    columns[col] = diagonals[row + col] = anti_diagonals[n - row + col] = 0
                    board[row][col] = "."

        result = []
        board = [["."] * n for _ in range(n)]
        columns = [0] * n
        diagonals = [0] * (2 * n)  # For diagonals (row + col)
        anti_diagonals = [0] * (2 * n)  # For anti-diagonals (n - row + col)

        backtrack(0)
        return result
