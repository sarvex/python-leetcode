from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

        Intuition: Use a direction-based approach to traverse the matrix in spiral order,
        changing direction when hitting boundaries or filled cells.

        Approach: Initialize a matrix with zeros. Move in the current direction until
        hitting a boundary or a filled cell, then rotate 90 degrees clockwise and continue.
        Fill each cell with consecutive integers from 1 to n^2.

        Complexity:
        Time: O(n^2) where n is the size of the matrix, as we visit each cell exactly once
        Space: O(n^2) for the result matrix
        """
        # Initialize matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define the four directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Initialize position and direction index
        row, col = 0, 0
        dir_idx = 0

        # Fill the matrix with values from 1 to n^2
        for value in range(1, n ** 2 + 1):
            # Fill current cell
            matrix[row][col] = value

            # Calculate next position
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]

            # Check if we need to change direction
            if (next_row < 0 or next_row >= n or
                    next_col < 0 or next_col >= n or
                    matrix[next_row][next_col] != 0):
                # Change direction clockwise
                dir_idx = (dir_idx + 1) % 4
                next_row = row + directions[dir_idx][0]
                next_col = col + directions[dir_idx][1]

            # Move to next position
            row, col = next_row, next_col

        return matrix
