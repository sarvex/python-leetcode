class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        """Compute block sum for each element within distance k.

        Intuition:
            Use a 2D prefix sum to answer rectangular range sum queries in O(1).

        Approach:
            Build a prefix sum matrix, then for each cell compute the sum of
            the block bounded by [i-k, j-k] to [i+k, j+k] using inclusion-exclusion.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i, row in enumerate(mat, 1):
            for j, val in enumerate(row, 1):
                prefix[i][j] = (
                    prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + val
                )
        answer = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                r1, c1 = max(i - k, 0), max(j - k, 0)
                r2, c2 = min(rows - 1, i + k), min(cols - 1, j + k)
                answer[i][j] = (
                    prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1]
                )
        return answer
