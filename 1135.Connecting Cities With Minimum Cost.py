class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        """Find the minimum cost to connect all cities.

        Intuition:
            This is a minimum spanning tree problem. Kruskal's algorithm with
            union-find efficiently finds the MST by processing edges in order
            of increasing cost.

        Approach:
            Sort edges by cost. Use union-find with path compression to greedily
            add the cheapest edge that connects two disjoint components. Stop
            early when all cities are connected.

        Complexity:
            Time: O(E log E) where E is the number of connections
            Space: O(n) for the parent array
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        connections.sort(key=lambda edge: edge[2])
        parent = list(range(n))
        total_cost = 0
        components = n
        for city_a, city_b, cost in connections:
            city_a -= 1
            city_b -= 1
            root_a, root_b = find(city_a), find(city_b)
            if root_a == root_b:
                continue
            parent[root_a] = root_b
            total_cost += cost
            components -= 1
            if components == 1:
                return total_cost
        return -1
