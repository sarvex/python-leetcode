# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

from bisect import bisect_left


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        """Find leftmost column containing a 1 using binary search per row.

        Intuition:
            Each row is sorted, so binary search finds the first 1 efficiently.

        Approach:
            Get matrix dimensions, then for each row binary search for the
            leftmost 1. Track the global minimum column index across all rows.

        Complexity:
            Time: O(m * log(n)) where m is rows and n is columns
            Space: O(1)
        """
        rows, cols = binaryMatrix.dimensions()
        result = cols
        for row in range(rows):
            col = bisect_left(range(cols), 1, key=lambda k: binaryMatrix.get(row, k))
            result = min(result, col)
        return -1 if result >= cols else result
