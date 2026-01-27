from itertools import pairwise


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with union by size and path compression."""

    def __init__(self, n: int) -> None:
        """Initialize with n elements."""
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        """Find root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """Union two elements by size. Returns False if already connected."""
        root_a, root_b = self.find(a - 1), self.find(b - 1)
        if root_a == root_b:
            return False
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        """Union-Find approach to dynamically count islands after each addition.

        Intuition:
            Each new land cell potentially creates a new island, but may also
            merge with adjacent existing islands via union-find.

        Approach:
            1. Initialize a union-find structure for the entire grid.
            2. For each position, mark it as land and increment the island count.
            3. Check all 4 neighbors; if a neighbor is land, union the two cells
               and decrement the count if they were in different components.
            4. Record the island count after each operation.

        Complexity:
            Time: O(k * α(m*n)) where k is number of positions and α is inverse Ackermann
            Space: O(m*n)
        """
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]
        result = []
        directions = (-1, 0, 1, 0, -1)
        count = 0
        for i, j in positions:
            if grid[i][j]:
                result.append(count)
                continue
            grid[i][j] = 1
            count += 1
            for delta_row, delta_col in pairwise(directions):
                neighbor_row, neighbor_col = i + delta_row, j + delta_col
                if (
                    0 <= neighbor_row < m
                    and 0 <= neighbor_col < n
                    and grid[neighbor_row][neighbor_col]
                    and uf.union(i * n + j, neighbor_row * n + neighbor_col)
                ):
                    count -= 1
            result.append(count)
        return result
