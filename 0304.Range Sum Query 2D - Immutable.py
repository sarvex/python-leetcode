class NumMatrix:
    """2D prefix sum matrix for immutable region sum queries.

    Uses a 2D prefix sum matrix to answer rectangular region sum queries
    in O(1) time after O(m*n) preprocessing.
    """

    def __init__(self, matrix: list[list[int]]) -> None:
        """Initialize with 2D prefix sum matrix.

        Args:
            matrix: The input 2D array of integers.
        """
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                self.prefix[i + 1][j + 1] = (
                    self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                    + val
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Return sum of elements in the rectangle defined by corners.

        Intuition:
            2D prefix sums enable O(1) rectangular region sum via inclusion-exclusion.

        Approach:
            Use inclusion-exclusion on the 2D prefix sum matrix.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            - self.prefix[row1][col2 + 1]
            + self.prefix[row1][col1]
        )
