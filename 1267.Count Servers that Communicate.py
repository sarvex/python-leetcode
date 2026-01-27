class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        """Count servers that can communicate with at least one other server.

        Intuition:
            A server communicates if there is another server in the same row
            or column. Precompute row and column server counts.

        Approach:
            First pass: count servers per row and per column. Second pass:
            a server communicates if its row count or column count exceeds 1.

        Complexity:
            Time: O(m * n)
            Space: O(m + n)
        """
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1
        return sum(
            grid[i][j] and (row_count[i] > 1 or col_count[j] > 1)
            for i in range(rows)
            for j in range(cols)
        )
