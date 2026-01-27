class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        """Brute-force matrix multiplication.

        Intuition:
            Standard matrix multiplication with three nested loops. For sparse
            matrices, many multiplications involve zero and could be skipped.

        Approach:
            1. Create result matrix of dimensions m x n.
            2. For each cell (i, j) in the result, compute the dot product
               of row i of mat1 and column j of mat2.

        Complexity:
            Time: O(m * n * k) where mat1 is m×k and mat2 is k×n
            Space: O(m * n) for the result matrix
        """
        rows, cols = len(mat1), len(mat2[0])
        result = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                for k in range(len(mat2)):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result
