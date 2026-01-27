from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]
    ) -> list[int]:
        """Find shortest path using alternating red and blue edges.

        Intuition:
            BFS from node 0 with two starting states (red and blue) ensures
            we explore shortest paths first while alternating edge colors.

        Approach:
            Build separate adjacency lists for red (0) and blue (1) edges.
            BFS with state (node, color), toggling color at each step.
            Track visited (node, color) pairs to avoid revisiting.

        Complexity:
            Time: O(n + E) where E is total number of edges
            Space: O(n + E) for adjacency lists and visited set
        """
        graph = [defaultdict(list), defaultdict(list)]
        for source, target in redEdges:
            graph[0][source].append(target)
        for source, target in blueEdges:
            graph[1][source].append(target)
        result = [-1] * n
        visited = set()
        queue = deque([(0, 0), (0, 1)])
        distance = 0
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if result[node] == -1:
                    result[node] = distance
                visited.add((node, color))
                next_color = color ^ 1
                for neighbor in graph[next_color][node]:
                    if (neighbor, next_color) not in visited:
                        queue.append((neighbor, next_color))
            distance += 1
        return result
