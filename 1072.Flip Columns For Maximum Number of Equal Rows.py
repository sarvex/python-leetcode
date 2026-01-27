from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        """Find max rows that can be made equal after flipping columns.

        Intuition:
            Two rows can become equal after flips if they are identical or
            complementary. Normalize each row by its first element.

        Approach:
            For each row, create a canonical form by XORing with the first element.
            Count occurrences of each canonical form and return the maximum.

        Complexity:
            Time: O(m * n) where m = rows, n = columns
            Space: O(m * n) for storing canonical forms
        """
        pattern_count: Counter[tuple[int, ...]] = Counter()
        for row in matrix:
            canonical = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            pattern_count[canonical] += 1
        return max(pattern_count.values())
