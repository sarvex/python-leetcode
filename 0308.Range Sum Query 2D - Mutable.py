class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree) for prefix sum queries with point updates."""

    def __init__(self, n: int) -> None:
        """Initialize tree with n elements."""
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        """Add delta to element at index x."""
        while x <= self.n:
            self.tree[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        """Return prefix sum from index 1 to x."""
        total = 0
        while x > 0:
            total += self.tree[x]
            x -= x & -x
        return total


class NumMatrix:
    """Mutable 2D matrix with region sum queries using per-row BITs.

    Each row maintains a separate Binary Indexed Tree for efficient
    point updates and range sum queries.
    """

    def __init__(self, matrix: list[list[int]]) -> None:
        """Initialize by building a BIT for each row.

        Args:
            matrix: The input 2D array of integers.
        """
        self.trees: list[BinaryIndexedTree] = []
        cols = len(matrix[0])
        for row in matrix:
            tree = BinaryIndexedTree(cols)
            for j, val in enumerate(row):
                tree.update(j + 1, val)
            self.trees.append(tree)

    def update(self, row: int, col: int, val: int) -> None:
        """Update element at (row, col) to val.

        Intuition:
            Compute delta from the current value and apply a point update.

        Approach:
            Query current value from the row's BIT, compute difference, update.

        Complexity:
            Time: O(log n) where n is the number of columns
            Space: O(1)
        """
        tree = self.trees[row]
        prev = tree.query(col + 1) - tree.query(col)
        tree.update(col + 1, val - prev)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Return sum of elements in the rectangle defined by corners.

        Intuition:
            Sum the range query results across all rows in the region.

        Approach:
            For each row from row1 to row2, query the column range sum using BIT.

        Complexity:
            Time: O(m * log n) where m is row range and n is number of columns
            Space: O(1)
        """
        return sum(
            tree.query(col2 + 1) - tree.query(col1)
            for tree in self.trees[row1 : row2 + 1]
        )
