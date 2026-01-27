class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """Dijkstra's algorithm (adjacency matrix) for shortest paths from source.

        Intuition:
            Find the shortest path from node k to all other nodes; the answer is
            the maximum of those distances.

        Approach:
            1. Build an adjacency matrix with edge weights.
            2. Run Dijkstra: repeatedly pick the unvisited node with the smallest
               distance, mark it visited, and relax its neighbors.
            3. Return max distance, or -1 if any node is unreachable.

        Complexity:
            Time: O(N^2)
            Space: O(N^2)
        """
        UNREACHABLE = 0x3F3F
        dist = [UNREACHABLE] * n
        visited = [False] * n
        graph = [[UNREACHABLE] * n for _ in range(n)]
        for source, target, weight in times:
            graph[source - 1][target - 1] = weight
        dist[k - 1] = 0
        for _ in range(n):
            nearest = -1
            for j in range(n):
                if not visited[j] and (nearest == -1 or dist[nearest] > dist[j]):
                    nearest = j
            visited[nearest] = True
            for j in range(n):
                dist[j] = min(dist[j], dist[nearest] + graph[nearest][j])
        result = max(dist)
        return -1 if result == UNREACHABLE else result
