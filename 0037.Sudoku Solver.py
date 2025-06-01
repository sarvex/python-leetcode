from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Backtracking with constraint propagation

        Intuition:
        Use backtracking to try different numbers for each empty cell while maintaining
        constraints for rows, columns, and 3x3 boxes. When we find a valid solution,
        we stop the search.

        Approach:
        1. Identify all empty cells that need to be filled
        2. Track which numbers are already used in each row, column, and 3x3 box
        3. Use backtracking to try different numbers for each empty cell
        4. When a valid solution is found, update the board and return

        Complexity:
        Time: O(9^m) where m is the number of empty cells (worst case)
        Space: O(m) for recursion stack + O(81) for tracking constraints = O(m)
        """
        # Track which numbers are used in each row, column, and 3x3 box
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        # Find all empty cells
        empty_cells: List[Tuple[int, int]] = []
        solution_found = False

        # Initialize constraints based on the given board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    # Convert '1'-'9' to 0-8 index
                    digit = int(board[i][j]) - 1
                    rows[i][digit] = cols[j][digit] = boxes[i // 3][j // 3][digit] = True

        def backtrack(cell_index: int) -> None:
            """Try filling empty cells recursively using backtracking."""
            nonlocal solution_found

            # Base case: all empty cells are filled
            if cell_index == len(empty_cells):
                solution_found = True
                return

            # Get current empty cell coordinates
            row, col = empty_cells[cell_index]
            box_row, box_col = row // 3, col // 3

            # Try each possible digit (1-9)
            for digit in range(9):
                # Check if this digit can be placed here
                if not (rows[row][digit] or cols[col][digit] or boxes[box_row][box_col][digit]):
                    # Place the digit and mark constraints
                    board[row][col] = str(digit + 1)
                    rows[row][digit] = cols[col][digit] = boxes[box_row][box_col][digit] = True

                    # Continue with next empty cell
                    backtrack(cell_index + 1)

                    # If solution is found, no need to backtrack further
                    if solution_found:
                        return

                    # Backtrack: remove the digit and constraints
                    board[row][col] = '.'
                    rows[row][digit] = cols[col][digit] = boxes[box_row][box_col][digit] = False

        # Start backtracking from the first empty cell
        backtrack(0)
