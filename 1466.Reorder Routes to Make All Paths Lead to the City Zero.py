from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        DFS with graph transformation

        Intuition:
        We need to count how many edges need to be reversed to make all paths lead to city 0.
        If we treat the graph as undirected, we can perform a DFS from city 0 and check the
        original direction of each edge we traverse. If an edge points away from city 0,
        it needs to be reversed.

        Approach:
        1. Build an undirected graph where each edge stores its original direction
           (1 if it needs to be reversed when traversing from 0, 0 if it's already correct)
        2. Perform DFS from city 0, counting edges that need to be reversed

        Complexity:
        Time: O(n) where n is the number of cities (edges = n-1 in a tree)
        Space: O(n) for the graph representation and recursion stack
        """
        def dfs(current: int, parent: int) -> int:
            # Sum the cost of all edges from current node to its children
            # plus the recursive cost from each child
            return sum(cost + dfs(neighbor, current)
                      for neighbor, cost in graph[current]
                      if neighbor != parent)

        # Build graph: for each edge, store the neighbor and whether the edge needs reversal
        graph = [[] for _ in range(n)]
        for from_city, to_city in connections:
            # Original edge (needs reversal when traversing from 0): cost = 1
            graph[from_city].append((to_city, 1))
            # Reverse edge (already points to parent): cost = 0
            graph[to_city].append((from_city, 0))

        # Start DFS from city 0 with no parent
        return dfs(0, -1)
