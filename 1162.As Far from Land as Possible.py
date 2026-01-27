from collections import deque
from itertools import pairwise


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """Find the water cell farthest from any land cell using multi-source BFS.

        Intuition:
            Start BFS simultaneously from all land cells. The last water cell
            reached is the farthest from any land.

        Approach:
            Enqueue all land cells. Perform level-order BFS, marking visited
            water cells. Track the number of BFS levels as the maximum distance.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        n = len(grid)
        queue = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        distance = -1
        if len(queue) in (0, n * n):
            return distance
        directions = (-1, 0, 1, 0, -1)
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for delta_r, delta_c in pairwise(directions):
                    new_row, new_col = row + delta_r, col + delta_c
                    if (
                        0 <= new_row < n
                        and 0 <= new_col < n
                        and grid[new_row][new_col] == 0
                    ):
                        grid[new_row][new_col] = 1
                        queue.append((new_row, new_col))
            distance += 1
        return distance
