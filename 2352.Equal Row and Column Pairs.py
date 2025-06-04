from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Matrix transposition with zip for elegant row-column comparison

        Intuition:
        Equal row and column pairs can be found by comparing rows with transposed columns.
        Python's zip(*grid) elegantly transposes the matrix in a single operation.

        Approach:
        1. Convert rows to tuples and count their occurrences
        2. Transpose the grid using zip(*grid) to get columns
        3. For each column tuple, check if it exists in the row counter

        Complexity:
        Time: O(n²) where n is the grid dimension
        Space: O(n²) for storing row patterns in the counter
        """
        row_counter = Counter(map(tuple, grid))
        col_tuples = map(tuple, zip(*grid))

        return sum(row_counter[col] for col in col_tuples)
