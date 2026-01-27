from collections import Counter
from itertools import pairwise


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        """DFS labeling islands then checking 0-cells for max merged island.

        Intuition:
            Label each island with a unique ID and record its size. For each
            0-cell, check adjacent island IDs and sum their sizes + 1.

        Approach:
            1. DFS to label all islands with unique root IDs and count sizes.
            2. The baseline answer is the largest island found.
            3. For each 0-cell, collect unique adjacent island IDs and compute
               the potential merged island size.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """

        def flood_fill(row: int, col: int) -> None:
            island_label[row][col] = current_root
            island_size[current_root] += 1
            for delta_r, delta_c in pairwise(directions):
                new_row, new_col = row + delta_r, col + delta_c
                if (
                    0 <= new_row < size
                    and 0 <= new_col < size
                    and grid[new_row][new_col]
                    and island_label[new_row][new_col] == 0
                ):
                    flood_fill(new_row, new_col)

        size = len(grid)
        island_size: Counter[int] = Counter()
        island_label = [[0] * size for _ in range(size)]
        directions = (-1, 0, 1, 0, -1)
        current_root = 0
        for row, grid_row in enumerate(grid):
            for col, cell in enumerate(grid_row):
                if cell and island_label[row][col] == 0:
                    current_root += 1
                    flood_fill(row, col)
        result = max(island_size.values() or [0])
        for row, grid_row in enumerate(grid):
            for col, cell in enumerate(grid_row):
                if cell == 0:
                    adjacent_islands: set[int] = set()
                    for delta_r, delta_c in pairwise(directions):
                        new_row, new_col = row + delta_r, col + delta_c
                        if 0 <= new_row < size and 0 <= new_col < size:
                            adjacent_islands.add(island_label[new_row][new_col])
                    result = max(
                        result, sum(island_size[root] for root in adjacent_islands) + 1
                    )
        return result
