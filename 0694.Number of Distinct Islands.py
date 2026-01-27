class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        """DFS with path encoding to identify distinct island shapes.

        Intuition:
            Two islands are the same shape if their DFS traversal paths are
            identical. Encoding the direction of each DFS step (and backtrack)
            creates a unique signature for each island shape.

        Approach:
            1. For each unvisited land cell, run DFS and record the traversal
               path as a string of direction codes.
            2. Include backtrack markers to distinguish different shapes.
            3. Add each path signature to a set.
            4. Return the size of the set.

        Complexity:
            Time: O(m * n) visiting each cell at most once
            Space: O(m * n) for the path signatures and recursion stack
        """

        def dfs(row: int, col: int, direction: int) -> None:
            grid[row][col] = 0
            path.append(str(direction))
            directions = (-1, 0, 1, 0, -1)
            for step in range(1, 5):
                next_row, next_col = row + directions[step - 1], col + directions[step]
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col]
                ):
                    dfs(next_row, next_col, step)
            path.append(str(-direction))

        island_shapes: set[str] = set()
        path: list[str] = []
        rows, cols = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    dfs(i, j, 0)
                    island_shapes.add("".join(path))
                    path.clear()
        return len(island_shapes)
