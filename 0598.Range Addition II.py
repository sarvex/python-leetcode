class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        """Find count of maximum elements after applying range addition operations.

        Intuition:
            Each operation increments a submatrix from (0,0) to (a,b). The
            maximum value cell is the intersection of all such submatrices,
            which is the smallest a and smallest b across all operations.

        Approach:
            1. Track the minimum row bound and column bound across all operations.
            2. The answer is the product of these minimums.
            3. If no operations, the entire matrix has the same value.

        Complexity:
            Time: O(k) where k is the number of operations
            Space: O(1)
        """
        for row_bound, col_bound in ops:
            m = min(m, row_bound)
            n = min(n, col_bound)
        return m * n
