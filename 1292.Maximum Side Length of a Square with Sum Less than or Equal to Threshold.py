class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        """Maximum side length of a square submatrix with sum at most threshold.

        Intuition:
            Use a 2D prefix sum to compute submatrix sums in O(1), then binary search
            for the largest valid square side length.

        Approach:
            Build a prefix sum matrix. Binary search on the side length, checking if
            any square of that size has a sum within the threshold using the prefix sum.

        Complexity:
            Time: O(m * n * log(min(m, n)))
            Space: O(m * n)
        """

        def has_valid_square(side: int) -> bool:
            for i in range(rows - side + 1):
                for j in range(cols - side + 1):
                    total = (
                        prefix[i + side][j + side]
                        - prefix[i][j + side]
                        - prefix[i + side][j]
                        + prefix[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i, row in enumerate(mat, 1):
            for j, value in enumerate(row, 1):
                prefix[i][j] = (
                    prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + value
                )

        left, right = 0, min(rows, cols)
        while left < right:
            mid = (left + right + 1) >> 1
            if has_valid_square(mid):
                left = mid
            else:
                right = mid - 1
        return left
