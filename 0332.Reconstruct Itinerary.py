from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """Hierholzer's algorithm for Eulerian path reconstruction.

        Intuition:
            The itinerary is an Eulerian path in a directed graph. By greedily
            visiting the smallest lexicographic destination and backtracking
            when stuck, we reconstruct the correct order.

        Approach:
            1. Build an adjacency list sorted in reverse lexicographic order
               so that popping gives the smallest destination.
            2. Perform DFS from 'JFK', appending airports post-visit.
            3. Reverse the result to get the correct itinerary order.

        Complexity:
            Time: O(E log E) where E is the number of tickets (for sorting)
            Space: O(E) for the graph and result
        """

        def search(airport: str) -> None:
            while graph[airport]:
                search(graph[airport].pop())
            itinerary.append(airport)

        graph: dict[str, list[str]] = defaultdict(list)
        for origin, destination in sorted(tickets, reverse=True):
            graph[origin].append(destination)
        itinerary: list[str] = []
        search("JFK")
        return itinerary[::-1]
