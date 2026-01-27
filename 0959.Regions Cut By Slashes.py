class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        """Union-Find on subdivided grid cells (4 triangles per cell).

        Intuition:
            Each cell is split into 4 triangles (top=0, right=1, bottom=2, left=3).
            Slashes divide certain triangles while spaces unite all four.
            Adjacent cells share triangle boundaries.

        Approach:
            1. Each cell contributes 4 regions (triangles).
            2. '/' unites top-left and bottom-right pairs.
            3. '\\' unites top-right and bottom-left pairs.
            4. ' ' unites all four triangles.
            5. Adjacent cells are connected: bottom to top, right to left.
            6. Count remaining distinct components.

        Complexity:
            Time: O(n^2 * α(n^2)) — union-find on 4*n^2 elements
            Space: O(n^2) — parent array for union-find
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_a] = root_b
                nonlocal region_count
                region_count -= 1

        grid_size = len(grid)
        region_count = grid_size * grid_size * 4
        parent = list(range(region_count))
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                cell = row * grid_size + col
                if row < grid_size - 1:
                    union(4 * cell + 2, (cell + grid_size) * 4)
                if col < grid_size - 1:
                    union(4 * cell + 1, (cell + 1) * 4 + 3)
                if char == "/":
                    union(4 * cell, 4 * cell + 3)
                    union(4 * cell + 1, 4 * cell + 2)
                elif char == "\\":
                    union(4 * cell, 4 * cell + 1)
                    union(4 * cell + 2, 4 * cell + 3)
                else:
                    union(4 * cell, 4 * cell + 1)
                    union(4 * cell + 1, 4 * cell + 2)
                    union(4 * cell + 2, 4 * cell + 3)
        return region_count
