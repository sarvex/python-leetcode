from math import inf


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distance_threshold: int
    ) -> int:
        """Find city with fewest reachable cities within threshold distance.

        Intuition:
            Run Dijkstra from each city and count reachable neighbors within
            the threshold. Return the highest-numbered city with the smallest count.

        Approach:
            Build adjacency matrix, run Dijkstra for each source city, count
            cities within threshold. Track the city with fewest neighbors,
            breaking ties by largest index.

        Complexity:
            Time: O(n^3) using simple Dijkstra without heap
            Space: O(n^2)
        """

        def dijkstra(source: int) -> int:
            dist = [inf] * n
            dist[source] = 0
            visited = [False] * n
            for _ in range(n):
                closest = -1
                for j in range(n):
                    if not visited[j] and (closest == -1 or dist[closest] > dist[j]):
                        closest = j
                visited[closest] = True
                for j in range(n):
                    if dist[closest] + graph[closest][j] < dist[j]:
                        dist[j] = dist[closest] + graph[closest][j]
            return sum(d <= distance_threshold for d in dist)

        graph = [[inf] * n for _ in range(n)]
        for source, target, weight in edges:
            graph[source][target] = graph[target][source] = weight
        best_city = n
        min_neighbors = inf
        for i in range(n - 1, -1, -1):
            if (neighbor_count := dijkstra(i)) < min_neighbors:
                min_neighbors, best_city = neighbor_count, i
        return best_city
