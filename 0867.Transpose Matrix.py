class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """Swap rows and columns using Python's zip unpacking.

        Intuition:
        Transposing a matrix swaps its rows and columns. Python's zip with
        unpacking naturally produces the transposed rows as tuples.

        Approach:
        1. Unpack matrix rows into zip to group elements by column index
        2. Convert each resulting tuple to a list

        Complexity:
        Time: O(m * n) where m is rows and n is columns
        Space: O(m * n) for the transposed matrix
        """
        return [list(row) for row in zip(*matrix)]
