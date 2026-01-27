class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """Count columns that are not sorted vertically.

        Intuition:
            A column should be deleted if any adjacent pair of rows has a
            character that is out of sorted order in that column.

        Approach:
            1. Iterate over each column index.
            2. For each column, check consecutive rows for sorted order.
            3. If any pair is out of order, increment the deletion count.

        Complexity:
            Time: O(n * m) — check each cell in the grid
            Space: O(1) — constant extra space
        """
        num_cols, num_rows = len(strs[0]), len(strs)
        deletions = 0
        for col in range(num_cols):
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    deletions += 1
                    break
        return deletions
