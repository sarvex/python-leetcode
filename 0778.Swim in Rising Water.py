class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """Binary search on answer combined with DFS path validation.

        Intuition
        ---------
        The minimum time needed is at least the maximum of start and end values.
        We can binary search on possible time values and check if a path exists
        where all cells have values <= that time.

        Approach
        --------
        1. Binary search on the time range [max(start, end), n*n-1]
        2. For each mid value, use DFS to check if we can reach destination
        3. Only visit cells with value <= current time threshold
        4. If reachable, try smaller times; otherwise try larger times

        Complexity
        ----------
        Time: O(n^2 * log(n^2)) where n is grid dimension
        Space: O(n^2) for visited set and recursion stack
        """
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r: int, c: int, max_time: int, visited: set[tuple[int, int]]) -> bool:
            """Check if destination is reachable within max_time."""
            if r == n - 1 and c == n - 1:
                return True

            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                    and grid[nr][nc] <= max_time
                ):
                    if dfs(nr, nc, max_time, visited):
                        return True

            return False

        s = max(grid[0][0], grid[n - 1][n - 1])
        e = n * n - 1
        res = e

        while s <= e:
            m = (s + e) // 2
            visited: set[tuple[int, int]] = set()

            if dfs(0, 0, m, visited):
                e = m - 1
                res = m
            else:
                s = m + 1

        return res
