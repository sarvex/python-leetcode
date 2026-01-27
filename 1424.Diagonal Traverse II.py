class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        """Traverse a 2D list along anti-diagonals from top-left to bottom-right.

        Intuition:
            Elements on the same anti-diagonal share the same (row + col) sum.
            Within a diagonal, lower rows come first.

        Approach:
            Collect all elements as (row + col, col, value) tuples. Sort by
            diagonal index then by column. Extract values in sorted order.

        Complexity:
            Time: O(n log n) where n is total number of elements
            Space: O(n) for the auxiliary array
        """
        entries: list[tuple[int, int, int]] = []
        for row, row_values in enumerate(nums):
            for col, value in enumerate(row_values):
                entries.append((row + col, col, value))
        entries.sort()
        return [value for _, _, value in entries]
