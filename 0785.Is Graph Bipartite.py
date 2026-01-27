class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """DFS coloring to check 2-colorability of the graph.

        Intuition:
            A graph is bipartite if and only if it can be 2-colored such that no
            two adjacent nodes share the same color. We attempt to color each
            component using DFS.

        Approach:
            1. Maintain a color array initialized to 0 (uncolored)
            2. For each uncolored node, start DFS with color 1
            3. Color the node and recurse on neighbors with the opposite color (3-c)
            4. If a neighbor already has the same color, graph is not bipartite

        Complexity:
            Time: O(V + E) where V is vertices and E is edges
            Space: O(V) for the color array and recursion stack
        """

        def dfs(node: int, assigned_color: int) -> bool:
            color[node] = assigned_color
            for neighbor in graph[node]:
                if not color[neighbor]:
                    if not dfs(neighbor, 3 - assigned_color):
                        return False
                elif color[neighbor] == assigned_color:
                    return False
            return True

        num_nodes = len(graph)
        color = [0] * num_nodes
        for node in range(num_nodes):
            if not color[node] and not dfs(node, 1):
                return False
        return True
