class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """Union-find via DFS to count connected components.

        Intuition:
            Each connected component can be discovered by performing a DFS from
            any unvisited node, marking all reachable nodes as visited.

        Approach:
            1. Build an adjacency list from the edge list.
            2. Iterate through all nodes; for each unvisited node, run DFS to
               mark its entire component as visited and count it.

        Complexity:
            Time: O(n + E) where E is the number of edges
            Space: O(n + E) for the adjacency list and visited set
        """

        def dfs(node: int) -> int:
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1

        graph: list[list[int]] = [[] for _ in range(n)]
        for source, target in edges:
            graph[source].append(target)
            graph[target].append(source)
        visited: set[int] = set()
        return sum(dfs(node) for node in range(n))
