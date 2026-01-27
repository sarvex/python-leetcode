class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """Union-Find to detect cycles and verify graph connectivity.

        Intuition:
            A valid tree with n nodes has exactly n-1 edges and no cycles.
            Union-Find efficiently detects cycles by checking if two nodes
            share the same root before merging.

        Approach:
            1. Initialize a parent array where each node is its own root.
            2. For each edge, find the roots of both endpoints.
            3. If they share a root, a cycle exists — return False.
            4. Otherwise, union them and decrement the component count.
            5. The graph is a valid tree if exactly one component remains.

        Complexity:
            Time: O(n * α(n)) where α is the inverse Ackermann function
            Space: O(n) for the parent array
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(n))
        for node_a, node_b in edges:
            root_a, root_b = find(node_a), find(node_b)
            if root_a == root_b:
                return False
            parent[root_a] = root_b
            n -= 1
        return n == 1
