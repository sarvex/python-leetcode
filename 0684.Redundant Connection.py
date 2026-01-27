class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """Union-Find to detect the edge that creates a cycle.

        Intuition:
            In a tree with n nodes, there are exactly n-1 edges. The extra edge
            creates a cycle. Union-Find can detect when connecting two nodes
            that already share the same root.

        Approach:
            1. Initialize a Union-Find structure with path compression.
            2. Process edges one by one, unioning the two endpoints.
            3. If both endpoints already share the same root, that edge is
               redundant and creates the cycle.

        Complexity:
            Time: O(n * α(n)) nearly linear with inverse Ackermann
            Space: O(n) for the parent array
        """

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        parent = list(range(1010))
        for node_a, node_b in edges:
            if find(node_a) == find(node_b):
                return [node_a, node_b]
            parent[find(node_a)] = find(node_b)
        return []
