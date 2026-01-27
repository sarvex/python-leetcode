class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        """Maximize enemies killed by a bomb using prefix sum in four directions.

        Intuition:
            For each empty cell, the number of enemies killed is the sum of
            enemies in its row and column segments (bounded by walls). We can
            precompute this by scanning in all four directions.

        Approach:
            Create a kill count grid. For each row, scan left-to-right and
            right-to-left, counting enemies between walls. For each column,
            scan top-to-bottom and bottom-to-top similarly. Each cell accumulates
            kills from all four directions. Return the maximum among empty cells.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(grid), len(grid[0])
        kill_count = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            enemies = 0
            for j in range(cols):
                if grid[i][j] == "W":
                    enemies = 0
                elif grid[i][j] == "E":
                    enemies += 1
                kill_count[i][j] += enemies
            enemies = 0
            for j in range(cols - 1, -1, -1):
                if grid[i][j] == "W":
                    enemies = 0
                elif grid[i][j] == "E":
                    enemies += 1
                kill_count[i][j] += enemies
        for j in range(cols):
            enemies = 0
            for i in range(rows):
                if grid[i][j] == "W":
                    enemies = 0
                elif grid[i][j] == "E":
                    enemies += 1
                kill_count[i][j] += enemies
            enemies = 0
            for i in range(rows - 1, -1, -1):
                if grid[i][j] == "W":
                    enemies = 0
                elif grid[i][j] == "E":
                    enemies += 1
                kill_count[i][j] += enemies
        return max(
            [
                kill_count[i][j]
                for i in range(rows)
                for j in range(cols)
                if grid[i][j] == "0"
            ],
            default=0,
        )
