from collections import defaultdict


class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        """Find the diameter (longest path) of an undirected tree.

        Intuition:
            The diameter of a tree can be found with two BFS/DFS passes:
            first find the farthest node from any starting node, then find
            the farthest node from that node.

        Approach:
            Build an adjacency list. Run DFS from node 0 to find the farthest
            node. Run DFS again from that node to find the actual diameter.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(node: int, parent: int, depth: int) -> None:
            nonlocal max_depth, farthest_node
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)
            if max_depth < depth:
                max_depth = depth
                farthest_node = node

        graph: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        max_depth = 0
        farthest_node = 0
        dfs(0, -1, 0)
        dfs(farthest_node, -1, 0)
        return max_depth
