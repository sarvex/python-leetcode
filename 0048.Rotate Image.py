from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Transpose and Reflect: Rotate the matrix by 90 degrees clockwise in-place

        Intuition:
        Rotating a matrix 90° clockwise can be achieved by first reflecting it across the
        middle horizontal line (upside down), then transposing it (swapping elements across
        the main diagonal).

        Approach:
        1. Reflect the matrix vertically (swap rows across the middle horizontal line)
        2. Transpose the matrix (swap elements across the main diagonal)

        Complexity:
        Time: O(n²) where n is the side length of the matrix
        Space: O(1) as we modify the matrix in-place
        """
        n = len(matrix)
        # Step 1: Reflect vertically (across middle horizontal line)
        for i in range(n >> 1):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

        # Step 2: Transpose (swap across the main diagonal)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
