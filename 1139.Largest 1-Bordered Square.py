class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:
        """Find the area of the largest square with all 1s on its border.

        Intuition:
            Precompute how far each cell extends downward and rightward with
            consecutive 1s, then check all possible square sizes.

        Approach:
            Build two prefix arrays: one for consecutive 1s going down and one
            going right. For each candidate square size (largest first), check
            if all four borders have sufficient consecutive 1s.

        Complexity:
            Time: O(m * n * min(m, n)) where m, n are grid dimensions
            Space: O(m * n) for the prefix arrays
        """
        rows, cols = len(grid), len(grid[0])
        down = [[0] * cols for _ in range(rows)]
        right = [[0] * cols for _ in range(rows)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if grid[i][j]:
                    down[i][j] = down[i + 1][j] + 1 if i + 1 < rows else 1
                    right[i][j] = right[i][j + 1] + 1 if j + 1 < cols else 1

        for size in range(min(rows, cols), 0, -1):
            for i in range(rows - size + 1):
                for j in range(cols - size + 1):
                    if (
                        down[i][j] >= size
                        and right[i][j] >= size
                        and right[i + size - 1][j] >= size
                        and down[i][j + size - 1] >= size
                    ):
                        return size * size
        return 0
