from functools import cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        """Optimized DP with memoized DFS and pruning

        Intuition
        ---------
        V-shaped diagonals alternate values (1 -> 2 -> 0 -> 2 -> ...). From any starting cell with 1,
        we may extend along one diagonal direction and optionally turn once to the adjacent diagonal.

        Approach
        --------
        Use DFS with memoization over state (x, y, turned, dir). At each step we either:
        - continue in the same direction if the next cell matches the required alternating value, or
        - if we haven't turned yet, turn to the adjacent diagonal and continue similarly.

        We also prune starts using a theoretical upper bound per direction so we avoid exploring
        states that cannot beat the current best.

        Complexity
        ----------
        Time: O(m * n * 4 * 2)
        Space: O(m * n * 4 * 2) for memoization
        """

        n, m = len(grid), len(grid[0])

        # Diagonal directions in clockwise order: ↘, ↙, ↖, ↗
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        # Next expected value given current cell value: 1->2, 2->0, 0->2
        nv = [2, 2, 0]

        @cache
        def helper(x: int, y: int, turned: bool, dir_idx: int) -> int:
            res = 1
            dx, dy = dirs[dir_idx]
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == nv[grid[x][y]]:
                res = helper(nx, ny, turned, dir_idx) + 1

            if not turned:
                ndir = (dir_idx + 1) % 4  # turn to adjacent diagonal (clockwise)
                dx, dy = dirs[ndir]
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == nv[grid[x][y]]:
                    res = max(res, helper(nx, ny, True, ndir) + 1)

            return res

        best = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue

                # Theoretical per-direction bounds; if it can't beat current best, skip exploring.
                # Matches dirs order (↘, ↙, ↖, ↗)
                bounds = (n - i, j + 1, i + 1, m - j)
                for d in range(4):
                    if bounds[d] > best:
                        best = max(best, helper(i, j, False, d))

        return best
