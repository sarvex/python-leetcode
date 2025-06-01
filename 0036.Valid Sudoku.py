from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Hash Set Validation - Using three sets of boolean arrays to track seen digits

        Intuition:
        Use separate tracking arrays for rows, columns, and 3x3 sub-boxes to validate
        if a digit appears more than once in any of these regions.

        Approach:
        1. Create three 9x9 boolean arrays to track digits in rows, columns, and sub-boxes
        2. Iterate through each cell in the 9x9 Sudoku board
        3. For each digit encountered, check if it's already seen in its row, column, or sub-box
        4. If a duplicate is found, return False; otherwise, mark the digit as seen
        5. Return True if the entire board is valid

        Complexity:
        Time: O(1) - We always process exactly 81 cells with constant-time operations
        Space: O(1) - We use three 9x9 boolean arrays of fixed size
        """
        # Initialize tracking arrays for rows, columns, and sub-boxes
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Validate each cell in the board
        for i in range(9):
            for j in range(9):
                cell = board[i][j]

                # Skip empty cells
                if cell == '.':
                    continue

                # Convert digit to 0-based index
                digit = int(cell) - 1

                # Calculate sub-box index (0-8)
                box_idx = (i // 3) * 3 + (j // 3)

                # Check if digit already exists in row, column, or sub-box
                if rows[i][digit] or cols[j][digit] or boxes[box_idx][digit]:
                    return False

                # Mark digit as seen in respective tracking arrays
                rows[i][digit] = True
                cols[j][digit] = True
                boxes[box_idx][digit] = True

        return True
