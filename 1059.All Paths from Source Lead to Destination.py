from collections import defaultdict
from functools import cache


class Solution:
    def leadsToDestination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        """Check if all paths from source lead to destination.

        Intuition:
            DFS from source; every path must end at destination with no outgoing
            edges, and cycles must not exist.

        Approach:
            Build adjacency list. Use DFS with cycle detection (visited set).
            A node is valid if it's the destination with no outgoing edges, or
            all its neighbors are valid.

        Complexity:
            Time: O(V + E)
            Space: O(V + E) for graph and recursion
        """

        @cache
        def dfs(node: int) -> bool:
            if node == destination:
                return not graph[node]
            if node in visited or not graph[node]:
                return False
            visited.add(node)
            return all(dfs(neighbor) for neighbor in graph[node])

        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
        visited: set[int] = set()
        return dfs(source)
