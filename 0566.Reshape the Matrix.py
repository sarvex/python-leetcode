class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """Reshape matrix to new dimensions using linear index mapping.

        Intuition:
            A matrix can be reshaped if the total number of elements matches.
            Map each linear index to its row/column in both the original and
            target shapes.

        Approach:
            1. Check if m * n == r * c; if not, return original matrix.
            2. For each linear index, compute source and destination positions.
            3. Fill the result matrix accordingly.

        Complexity:
            Time: O(m * n)
            Space: O(r * c)
        """
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c:
            return mat
        result = [[0] * c for _ in range(r)]
        for i in range(rows * cols):
            result[i // c][i % c] = mat[i // cols][i % cols]
        return result
