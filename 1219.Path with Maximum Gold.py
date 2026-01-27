from itertools import pairwise


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """Path with maximum gold using backtracking DFS.

        Intuition:
            Try starting DFS from every cell with gold, exploring all four
            directions while avoiding revisited cells.

        Approach:
            For each cell, perform DFS marking cells as visited by zeroing them
            out, then restoring after exploration. Track maximum gold collected.

        Complexity:
            Time: O(m * n * 4^g) where g is the number of gold cells
            Space: O(g) for recursion depth
        """

        def dfs(row: int, col: int) -> int:
            if not (0 <= row < rows and 0 <= col < cols and grid[row][col]):
                return 0
            gold = grid[row][col]
            grid[row][col] = 0
            max_gold = (
                max(dfs(row + dr, col + dc) for dr, dc in pairwise(directions)) + gold
            )
            grid[row][col] = gold
            return max_gold

        rows, cols = len(grid), len(grid[0])
        directions = (-1, 0, 1, 0, -1)
        return max(dfs(i, j) for i in range(rows) for j in range(cols))
