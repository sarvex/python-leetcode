class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        """Minimum cost to supply water using Kruskal's algorithm with union-find.

        Intuition:
            Model wells as edges from a virtual node 0 to each house. Then the
            problem becomes finding the minimum spanning tree of this graph.

        Approach:
            Add virtual edges from node 0 for each well cost. Sort all edges
            by cost and apply Kruskal's algorithm with union-find to build the
            minimum spanning tree.

        Complexity:
            Time: O(E log E) where E is the number of edges
            Space: O(n)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i, well_cost in enumerate(wells, 1):
            pipes.append([0, i, well_cost])
        pipes.sort(key=lambda edge: edge[2])
        parent = list(range(n + 1))
        total_cost = 0
        for node_a, node_b, cost in pipes:
            root_a, root_b = find(node_a), find(node_b)
            if root_a != root_b:
                parent[root_a] = root_b
                n -= 1
                total_cost += cost
                if n == 0:
                    return total_cost
        return total_cost
