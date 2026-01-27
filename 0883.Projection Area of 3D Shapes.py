class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        """Sum of three orthogonal projections of 3D grid shapes.

        Intuition:
            The xy-projection counts non-zero cells, the yz-projection takes
            row maxima, and the zx-projection takes column maxima.

        Approach:
            1. xy area: count all cells with height > 0.
            2. yz area: sum the maximum height in each row.
            3. zx area: sum the maximum height in each column (via transpose).

        Complexity:
            Time: O(n * m)
            Space: O(1)
        """
        xy_area = sum(height > 0 for row in grid for height in row)
        yz_area = sum(max(row) for row in grid)
        zx_area = sum(max(column) for column in zip(*grid))
        return xy_area + yz_area + zx_area
