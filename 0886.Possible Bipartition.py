from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        """DFS graph coloring to check bipartiteness.

        Intuition:
            Model dislikes as an undirected graph. The partition is possible
            if and only if the graph is bipartite (2-colorable).

        Approach:
            1. Build an adjacency list from the dislikes pairs.
            2. Use DFS to try 2-coloring the graph.
            3. If any neighbor has the same color as the current node, return False.
            4. Process all connected components.

        Complexity:
            Time: O(n + E) where E is the number of dislike pairs.
            Space: O(n + E)
        """

        def dfs(node: int, assigned_color: int) -> bool:
            color[node] = assigned_color
            for neighbor in graph[node]:
                if color[neighbor] == assigned_color:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, 3 - assigned_color):
                    return False
            return True

        graph: dict[int, list[int]] = defaultdict(list)
        color = [0] * n
        for person_a, person_b in dislikes:
            person_a, person_b = person_a - 1, person_b - 1
            graph[person_a].append(person_b)
            graph[person_b].append(person_a)
        return all(node_color or dfs(node, 1) for node, node_color in enumerate(color))
