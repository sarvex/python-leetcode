from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Binary search each row for target in a sorted 2D matrix.

        Intuition:
            Each row is sorted, so we can binary search within each row
            to find the target efficiently.

        Approach:
            Iterate over each row and perform binary search using bisect_left.
            If the found index is within bounds and the value matches, return True.

        Complexity:
            Time: O(m log n) where m is rows and n is columns
            Space: O(1)
        """
        for row in matrix:
            col = bisect_left(row, target)
            if col < len(matrix[0]) and row[col] == target:
                return True
        return False
