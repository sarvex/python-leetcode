from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        """Find minimum time to collect all apples and return to root.

        Intuition:
            DFS from the root; an edge is traversed only if the subtree
            contains at least one apple.

        Approach:
            Build an adjacency list. DFS from node 0, tracking visited nodes.
            For each child, add its subtree cost. If a node has an apple or
            its subtree does, include the round-trip cost of 2 for its edge.

        Complexity:
            Time: O(n) visiting each node once
            Space: O(n) for adjacency list and visited array
        """

        def dfs(node: int, travel_cost: int) -> int:
            if visited[node]:
                return 0
            visited[node] = True
            subtree_cost = 0
            for neighbor in adjacency[node]:
                subtree_cost += dfs(neighbor, 2)
            if not hasApple[node] and subtree_cost == 0:
                return 0
            return travel_cost + subtree_cost

        adjacency: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
        visited = [False] * n
        return dfs(0, 0)
