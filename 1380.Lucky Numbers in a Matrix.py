class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        """Find lucky numbers: minimum in their row and maximum in their column.

        Intuition:
            A lucky number must be both a row minimum and a column maximum.
            The intersection of these two sets gives the answer.

        Approach:
            Compute the set of row minimums and the set of column maximums.
            Return their intersection as a list.

        Complexity:
            Time: O(m * n) where m is rows and n is columns.
            Space: O(m + n)
        """
        row_minimums = {min(row) for row in matrix}
        col_maximums = {max(col) for col in zip(*matrix)}
        return list(row_minimums & col_maximums)
