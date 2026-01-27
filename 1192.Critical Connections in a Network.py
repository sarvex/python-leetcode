class Solution:
    def criticalConnections(
        self, n: int, connections: list[list[int]]
    ) -> list[list[int]]:
        """Find all critical connections (bridges) using Tarjan's algorithm.

        Intuition:
            An edge is a bridge if the subtree rooted at one endpoint has no
            back edge to an ancestor of the other endpoint.

        Approach:
            Run DFS assigning discovery times. Track the lowest reachable
            discovery time (low value) for each node. If a child's low value
            exceeds the parent's discovery time, the edge is a bridge.

        Complexity:
            Time: O(V + E)
            Space: O(V + E)
        """

        def dfs(node: int, parent: int) -> None:
            nonlocal timer
            timer += 1
            discovery[node] = low[node] = timer
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not discovery[neighbor]:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > discovery[node]:
                        bridges.append([node, neighbor])
                else:
                    low[node] = min(low[node], discovery[neighbor])

        graph: list[list[int]] = [[] for _ in range(n)]
        for node_a, node_b in connections:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        discovery = [0] * n
        low = [0] * n
        timer = 0
        bridges: list[list[int]] = []
        dfs(0, -1)
        return bridges
