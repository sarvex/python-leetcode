class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        """Find minimum cables to move to connect all computers.

        Intuition:
            Count redundant cables (forming cycles) and connected components
            using Union-Find. We need (components - 1) cables to connect everything.

        Approach:
            Use Union-Find with path compression. Count redundant edges (where
            both endpoints share the same root). Return -1 if redundant edges
            are fewer than (components - 1).

        Complexity:
            Time: O(n + E * α(n)) where E is number of connections
            Space: O(n)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        redundant = 0
        components = n
        parent = list(range(n))
        for node_a, node_b in connections:
            root_a, root_b = find(node_a), find(node_b)
            if root_a == root_b:
                redundant += 1
            else:
                parent[root_a] = root_b
                components -= 1
        return -1 if components - 1 > redundant else components - 1
