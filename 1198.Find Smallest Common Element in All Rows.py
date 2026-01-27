from collections import Counter


class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        """Find the smallest element common to all rows in a sorted matrix.

        Intuition:
            Count element occurrences across all rows. The first element whose
            count equals the number of rows is the smallest common element.

        Approach:
            Iterate through the matrix row by row, counting each element. Since
            rows are sorted, the first element reaching a count equal to the
            number of rows is the answer.

        Complexity:
            Time: O(m * n) where m is rows and n is columns
            Space: O(m * n)
        """
        element_count: Counter[int] = Counter()
        num_rows = len(mat)
        for row in mat:
            for value in row:
                element_count[value] += 1
                if element_count[value] == num_rows:
                    return value
        return -1
