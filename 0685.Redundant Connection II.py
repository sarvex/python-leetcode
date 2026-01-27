class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.count = size

    def union(self, node_a: int, node_b: int) -> bool:
        if self.find(node_a) == self.find(node_b):
            return False
        self.parent[self.find(node_a)] = self.find(node_b)
        self.count -= 1
        return True

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        """Union-Find with conflict and cycle detection for directed graphs.

        Intuition:
            In a rooted tree, each node except root has exactly one parent. The
            extra edge either creates a node with two parents (conflict), a
            cycle, or both. We must identify the correct edge to remove.

        Approach:
            1. Track parent of each node. If a node gets a second parent, mark
               a conflict edge.
            2. Use Union-Find to detect cycles while skipping the conflict edge.
            3. If no conflict, return the cycle edge. If conflict and no cycle,
               return the conflict edge. If both, return the first parent edge
               of the conflicted node.

        Complexity:
            Time: O(n * α(n)) nearly linear
            Space: O(n) for parent arrays and Union-Find
        """
        num_edges = len(edges)
        node_parent = list(range(num_edges + 1))
        uf = UnionFind(num_edges + 1)
        conflict = cycle = None
        for i, (source, target) in enumerate(edges):
            if node_parent[target] != target:
                conflict = i
            else:
                node_parent[target] = source
                if not uf.union(source, target):
                    cycle = i
        if conflict is None:
            return edges[cycle]
        target = edges[conflict][1]
        if cycle is not None:
            return [node_parent[target], target]
        return edges[conflict]
