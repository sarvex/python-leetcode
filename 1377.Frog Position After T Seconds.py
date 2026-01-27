from collections import defaultdict, deque


class Solution:
    def frogPosition(
        self, n: int, edges: list[list[int]], t: int, target: int
    ) -> float:
        """Find the probability that a frog is on the target vertex after t seconds.

        Intuition:
            BFS from vertex 1 simulates the frog's movement. At each step the
            frog jumps to an unvisited neighbor with equal probability. If it
            reaches the target, it stays only if it has no unvisited neighbors
            or time runs out exactly.

        Approach:
            Build an adjacency list and BFS level by level. Track the
            probability at each node. When the target is reached, return the
            probability if the frog would stay (no children or no remaining
            time), otherwise return 0.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        graph: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue: deque[tuple[int, float]] = deque([(1, 1.0)])
        visited = [False] * (n + 1)
        visited[1] = True

        while queue and t >= 0:
            for _ in range(len(queue)):
                node, probability = queue.popleft()
                unvisited_children = len(graph[node]) - int(node != 1)
                if node == target:
                    return probability if unvisited_children * t == 0 else 0
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, probability / unvisited_children))
            t -= 1

        return 0
