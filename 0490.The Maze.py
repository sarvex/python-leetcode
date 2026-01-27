class Solution:
    def hasPath(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> bool:
        """DFS simulating ball rolling until hitting walls.

        Intuition:
            The ball rolls in a direction until hitting a wall. From each
            stopping point, try all four directions. Use DFS with a visited
            matrix to avoid revisiting positions.

        Approach:
            From each cell, roll the ball in all four directions until it
            hits a boundary or wall. Mark stopping positions as visited
            and recurse from there. Return True if the destination is
            reached.

        Complexity:
            Time: O(m * n) — each cell visited at most once
            Space: O(m * n) for the visited matrix
        """

        def dfs(row: int, col: int) -> None:
            if visited[row][col]:
                return
            visited[row][col] = True
            if [row, col] == destination:
                return
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row, col
                while (
                    0 <= new_row + delta_row < rows
                    and 0 <= new_col + delta_col < cols
                    and maze[new_row + delta_row][new_col + delta_col] == 0
                ):
                    new_row, new_col = new_row + delta_row, new_col + delta_col
                dfs(new_row, new_col)

        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]
        dfs(start[0], start[1])
        return visited[destination[0]][destination[1]]
