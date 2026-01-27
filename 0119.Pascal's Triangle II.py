class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """In-Place Dynamic Programming Approach

        Intuition:
            Each element in Pascal's triangle is the sum of the two elements
            above it. We can build a single row iteratively by updating it
            in-place from right to left to avoid overwriting values we still need.

        Approach:
            Initialize a row of ones with length rowIndex + 1. For each row from
            2 to rowIndex, update elements from right to left by adding the
            previous element.

        Complexity:
            Time: O(rowIndex^2)
            Space: O(rowIndex) for the result row
        """
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row
