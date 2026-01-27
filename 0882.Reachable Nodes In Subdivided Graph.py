import math
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        """Modified Dijkstra counting reachable original and subdivided nodes.

        Intuition:
            Treat subdivided edges as weighted edges. Use Dijkstra to find
            shortest distances, then count how many subdivided nodes on each
            edge are reachable from both endpoints.

        Approach:
            1. Build an adjacency list with edge weights equal to subdivided
               node count + 1.
            2. Run Dijkstra from node 0 to compute shortest distances.
            3. Count all original nodes within maxMoves distance.
            4. For each edge, count reachable subdivided nodes from both
               endpoints, capping at the total subdivided count.

        Complexity:
            Time: O(E log V)
            Space: O(V + E)
        """
        graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for source, dest, count in edges:
            graph[source].append((dest, count + 1))
            graph[dest].append((source, count + 1))
        priority_queue = [(0, 0)]
        dist = [0] + [math.inf] * n
        while priority_queue:
            distance, node = heappop(priority_queue)
            for neighbor, weight in graph[node]:
                if (new_dist := distance + weight) < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(priority_queue, (new_dist, neighbor))
        reachable = sum(d <= maxMoves for d in dist)
        for source, dest, count in edges:
            from_source = min(count, max(0, maxMoves - dist[source]))
            from_dest = min(count, max(0, maxMoves - dist[dest]))
            reachable += min(count, from_source + from_dest)
        return reachable
