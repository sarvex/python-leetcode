from itertools import pairwise


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        """Find path maximizing the minimum value using Union-Find with sorting.

        Intuition:
            Process cells from largest to smallest value. As we add each cell,
            union it with already-visited neighbors. The answer is the value of
            the cell that first connects top-left to bottom-right.

        Approach:
            Collect all cells with their values and sort them. Process cells
            in descending order, marking them visited and unioning with visited
            neighbors. Once (0,0) and (m-1,n-1) share a root, return the
            current cell's value.

        Complexity:
            Time: O(m * n * log(m * n)) for sorting all cells
            Space: O(m * n) for parent array and visited set
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols))
        cells = [
            (value, r, c) for r, row in enumerate(grid) for c, value in enumerate(row)
        ]
        cells.sort()
        result = 0
        directions = (-1, 0, 1, 0, -1)
        visited: set[tuple[int, int]] = set()
        while find(0) != find(rows * cols - 1):
            value, r, c = cells.pop()
            result = value
            visited.add((r, c))
            for dr, dc in pairwise(directions):
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    parent[find(r * cols + c)] = find(nr * cols + nc)
        return result
