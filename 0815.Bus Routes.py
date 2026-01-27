from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        """BFS on route graph to find minimum bus transfers.

        Intuition:
            Build a graph where routes are nodes connected if they share a stop.
            BFS from all routes containing the source stop to find the minimum
            number of buses to reach the target.

        Approach:
            1. Map each stop to its list of route indices.
            2. Build an adjacency list between routes sharing stops.
            3. BFS from source routes, checking if any route contains the target.

        Complexity:
            Time: O(n^2 * m) where n = number of routes, m = average route length
            Space: O(n^2 + total stops)
        """
        if source == target:
            return 0
        route_sets = [set(route) for route in routes]
        stop_to_routes: defaultdict[int, list[int]] = defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(route_idx)
        route_graph: defaultdict[int, list[int]] = defaultdict(list)
        for route_indices in stop_to_routes.values():
            num_routes = len(route_indices)
            for i in range(num_routes):
                for j in range(i + 1, num_routes):
                    route_a, route_b = route_indices[i], route_indices[j]
                    route_graph[route_a].append(route_b)
                    route_graph[route_b].append(route_a)
        queue = deque(stop_to_routes[source])
        transfers = 1
        visited: set[int] = set(stop_to_routes[source])
        while queue:
            for _ in range(len(queue)):
                route_idx = queue.popleft()
                if target in route_sets[route_idx]:
                    return transfers
                for neighbor in route_graph[route_idx]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            transfers += 1
        return -1
