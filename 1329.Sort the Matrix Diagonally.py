class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        """Sort each diagonal of the matrix in ascending order.

        Intuition:
            Elements on the same diagonal share the same (row - col) offset.
            Group by diagonal, sort, then place back.

        Approach:
            Collect elements into diagonal groups indexed by (rows - row + col).
            Sort each group in reverse so we can pop from the end efficiently.
            Reassign elements back to the matrix.

        Complexity:
            Time: O(m * n * log(min(m, n)))
            Space: O(m * n)
        """
        rows, cols = len(mat), len(mat[0])
        diagonals: list[list[int]] = [[] for _ in range(rows + cols)]
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                diagonals[rows - i + j].append(val)
        for diagonal in diagonals:
            diagonal.sort(reverse=True)
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = diagonals[rows - i + j].pop()
        return mat
