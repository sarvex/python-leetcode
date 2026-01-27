class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        """Increase buildings to min of row max and column max.

        Intuition:
            Each building can grow up to the minimum of its row maximum and
            column maximum without changing the skyline from any direction.

        Approach:
            1. Compute the maximum height for each row and each column.
            2. For each building, the allowed height is min(row_max, col_max).
            3. Sum all increases.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        return sum(
            min(row_max[i], col_max[j]) - height
            for i, row in enumerate(grid)
            for j, height in enumerate(row)
        )
