class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        """Check if a valid path exists from top-left to bottom-right.

        Intuition:
            Use Union-Find to connect cells that share a valid street
            connection based on their street types.

        Approach:
            For each cell, determine which directions its street type connects
            to (left, right, up, down). Union adjacent cells if both street
            types allow the connection. Finally check if top-left and
            bottom-right are in the same connected component.

        Complexity:
            Time: O(m * n * α(m * n)) with path compression
            Space: O(m * n) for the parent array
        """
        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def connect_left(row: int, col: int) -> None:
            if col > 0 and grid[row][col - 1] in (1, 4, 6):
                parent[find(row * cols + col)] = find(row * cols + col - 1)

        def connect_right(row: int, col: int) -> None:
            if col < cols - 1 and grid[row][col + 1] in (1, 3, 5):
                parent[find(row * cols + col)] = find(row * cols + col + 1)

        def connect_up(row: int, col: int) -> None:
            if row > 0 and grid[row - 1][col] in (2, 3, 4):
                parent[find(row * cols + col)] = find((row - 1) * cols + col)

        def connect_down(row: int, col: int) -> None:
            if row < rows - 1 and grid[row + 1][col] in (2, 5, 6):
                parent[find(row * cols + col)] = find((row + 1) * cols + col)

        for row in range(rows):
            for col in range(cols):
                street = grid[row][col]
                if street == 1:
                    connect_left(row, col)
                    connect_right(row, col)
                elif street == 2:
                    connect_up(row, col)
                    connect_down(row, col)
                elif street == 3:
                    connect_left(row, col)
                    connect_down(row, col)
                elif street == 4:
                    connect_right(row, col)
                    connect_down(row, col)
                elif street == 5:
                    connect_left(row, col)
                    connect_up(row, col)
                else:
                    connect_right(row, col)
                    connect_up(row, col)
        return find(0) == find(rows * cols - 1)
