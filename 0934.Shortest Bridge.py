from collections import deque
from itertools import pairwise


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        """DFS to find first island, BFS to expand to second island.

        Intuition:
            Find one island using DFS, then use multi-source BFS to expand
            outward from it until reaching the second island. The BFS level
            at which we first reach a cell of the second island is the answer.

        Approach:
            1. Find any cell of the first island.
            2. DFS to mark all cells of the first island and enqueue them.
            3. BFS level by level, expanding into water cells.
            4. Return the level count when a cell of the second island is reached.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """

        def flood_fill(row: int, col: int) -> None:
            queue.append((row, col))
            grid[row][col] = 2
            for delta_r, delta_c in pairwise(directions):
                next_row, next_col = row + delta_r, col + delta_c
                if (
                    0 <= next_row < size
                    and 0 <= next_col < size
                    and grid[next_row][next_col] == 1
                ):
                    flood_fill(next_row, next_col)

        size = len(grid)
        directions = (-1, 0, 1, 0, -1)
        queue: deque[tuple[int, int]] = deque()
        start_row, start_col = next(
            (row, col) for row in range(size) for col in range(size) if grid[row][col]
        )
        flood_fill(start_row, start_col)
        distance = 0
        while True:
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                for delta_r, delta_c in pairwise(directions):
                    next_row, next_col = curr_row + delta_r, curr_col + delta_c
                    if 0 <= next_row < size and 0 <= next_col < size:
                        if grid[next_row][next_col] == 1:
                            return distance
                        if grid[next_row][next_col] == 0:
                            grid[next_row][next_col] = 2
                            queue.append((next_row, next_col))
            distance += 1
