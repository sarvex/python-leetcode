class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """Bellman-Ford relaxation limited to k+1 iterations.

        Intuition:
            Bellman-Ford naturally handles edge-count constraints. By running
            exactly k+1 relaxation rounds and using a backup copy of distances,
            we ensure paths use at most k+1 edges (k intermediate stops).

        Approach:
            1. Initialize distances to infinity, source distance to 0
            2. For k+1 iterations, copy distances and relax all edges using
               the previous iteration's values
            3. Return destination distance or -1 if unreachable

        Complexity:
            Time: O(k * E) where E is the number of flights
            Space: O(n) for the distance array
        """
        INF = 0x3F3F3F3F
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            backup = dist.copy()
            for origin, destination, price in flights:
                dist[destination] = min(dist[destination], backup[origin] + price)
        return -1 if dist[dst] == INF else dist[dst]
