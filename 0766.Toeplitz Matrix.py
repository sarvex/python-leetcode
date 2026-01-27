class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """Check all diagonals share the same value by comparing adjacent rows.

        Intuition:
            A Toeplitz matrix has the property that every element equals the one
            diagonally above-left. We only need to verify each cell against its
            top-left neighbor.

        Approach:
            1. Iterate over every cell starting from row 1, column 1
            2. Compare matrix[i][j] with matrix[i-1][j-1]
            3. Return False immediately if any mismatch is found

        Complexity:
            Time: O(m * n) where m and n are matrix dimensions
            Space: O(1)
        """
        rows, cols = len(matrix), len(matrix[0])
        return all(
            matrix[i][j] == matrix[i - 1][j - 1]
            for i in range(1, rows)
            for j in range(1, cols)
        )
