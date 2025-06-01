from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Spiral traversal of a matrix

        Intuition:
        Traverse the matrix in a spiral order by moving in four directions: right, down, left, up.
        Use a visited set to track cells we've already processed and change direction when needed.

        Approach:
        1. Define the four directions as offsets: right (0,1), down (1,0), left (0,-1), up (-1,0)
        2. Start from the top-left corner and move in the current direction
        3. When we hit a boundary or a visited cell, change direction
        4. Continue until all cells are visited

        Complexity:
        Time: O(m*n) where m and n are the dimensions of the matrix
        Space: O(m*n) for the visited set and result list
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []
        visited = set()

        # Direction vectors: right, down, left, up
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_idx = 0
        row = col = 0

        def next_position(r: int, c: int, di: int) -> tuple[int, int]:
            return r + directions[di][0], c + directions[di][1]

        for _ in range(m * n):
            result.append(matrix[row][col])
            visited.add((row, col))

            # Calculate next position
            next_row, next_col = next_position(row, col, dir_idx)

            # Change direction if needed
            if (next_row < 0 or next_row >= m or
                    next_col < 0 or next_col >= n or
                    (next_row, next_col) in visited):
                dir_idx = (dir_idx + 1) % 4
                next_row, next_col = next_position(row, col, dir_idx)

            row, col = next_row, next_col

        return result
