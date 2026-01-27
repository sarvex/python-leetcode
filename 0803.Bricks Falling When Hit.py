from copy import deepcopy


class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        """Reverse-time Union-Find to count falling bricks.

        Intuition:
            Process hits in reverse: add bricks back and count how many newly
            connect to the top row. Union-Find tracks connected components
            and their sizes.

        Approach:
            1. Remove all hit bricks from a copy of the grid.
            2. Build Union-Find connecting remaining bricks; top row connects to a virtual root.
            3. Add bricks back in reverse order, unioning with neighbors.
            4. The increase in root component size (minus 1 for the brick itself) is the answer.

        Complexity:
            Time: O(m * n * alpha(m * n) + h * alpha(m * n)) where h = len(hits)
            Space: O(m * n)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                size[root_b] += size[root_a]
                parent[root_a] = root_b

        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols + 1))
        size = [1] * len(parent)
        modified_grid = deepcopy(grid)
        for row, col in hits:
            modified_grid[row][col] = 0
        for col in range(cols):
            if modified_grid[0][col] == 1:
                union(col, rows * cols)
        for row in range(1, rows):
            for col in range(cols):
                if modified_grid[row][col] == 0:
                    continue
                if modified_grid[row - 1][col] == 1:
                    union(row * cols + col, (row - 1) * cols + col)
                if col > 0 and modified_grid[row][col - 1] == 1:
                    union(row * cols + col, row * cols + col - 1)
        result: list[int] = []
        for row, col in reversed(hits):
            if grid[row][col] == 0:
                result.append(0)
                continue
            modified_grid[row][col] = 1
            prev_size = size[find(rows * cols)]
            if row == 0:
                union(col, rows * cols)
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                neighbor_row, neighbor_col = row + delta_row, col + delta_col
                if (
                    0 <= neighbor_row < rows
                    and 0 <= neighbor_col < cols
                    and modified_grid[neighbor_row][neighbor_col] == 1
                ):
                    union(row * cols + col, neighbor_row * cols + neighbor_col)
            curr_size = size[find(rows * cols)]
            result.append(max(0, curr_size - prev_size - 1))
        return result[::-1]
