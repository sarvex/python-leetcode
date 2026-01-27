class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            self.rank[root_a] += self.rank[root_b]
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += self.rank[root_a]
        return True


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """Union-Find to count removable stones by connected components.

        Intuition:
            Stones sharing a row or column are connected. Within each connected
            component of size k, we can remove k-1 stones. So the answer is
            total stones minus the number of connected components.

        Approach:
            1. Initialize Union-Find for all stones.
            2. For each pair of stones, union them if they share a row or column.
            3. Count successful unions — each union represents one removable stone.

        Complexity:
            Time: O(n^2 * α(n)) — pairwise comparison with near-constant union-find
            Space: O(n) — Union-Find storage
        """
        uf = UnionFind(len(stones))
        removals = 0
        for i, (row1, col1) in enumerate(stones):
            for j, (row2, col2) in enumerate(stones[:i]):
                if row1 == row2 or col1 == col2:
                    removals += uf.union(i, j)
        return removals
