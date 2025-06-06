from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """DFS approach to find connected components in an undirected graph

        Intuition:
        The problem can be modeled as finding the number of connected components
        in an undirected graph where cities are nodes and connections are edges.

        Approach:
        Use depth-first search to explore all cities connected to each unvisited city.
        Each time we start a new DFS, we've found a new province.

        Complexity:
        Time: O(n²) where n is the number of cities
        Space: O(n) for the visited array and recursion stack
        """
        def dfs(i: int) -> None:
            visited[i] = True
            for j, connected in enumerate(isConnected[i]):
                if not visited[j] and connected:
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces

    def findCircleNum_bfs(self, isConnected: List[List[int]]) -> int:
        """BFS approach to find connected components in an undirected graph

        Intuition:
        Similar to DFS, but using breadth-first search instead of recursion.

        Approach:
        Use a queue to explore all cities connected to each unvisited city level by level.
        Each time we start a new BFS, we've found a new province.

        Complexity:
        Time: O(n²) where n is the number of cities
        Space: O(n) for the visited array and queue
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                queue = deque([i])
                visited[i] = True

                while queue:
                    city = queue.popleft()
                    for neighbor, connected in enumerate(isConnected[city]):
                        if connected and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

        return provinces

    def findCircleNum_union_find(self, isConnected: List[List[int]]) -> int:
        """Union-Find approach to find connected components

        Intuition:
        We can use a disjoint set (Union-Find) data structure to track connected cities.
        Each city starts in its own set, and we merge sets when cities are connected.

        Approach:
        1. Initialize each city as its own parent
        2. For each pair of connected cities, union their sets
        3. Count the number of unique parents (provinces)

        Complexity:
        Time: O(n² * α(n)) where α is the inverse Ackermann function (nearly constant)
        Space: O(n) for the parent array
        """
        n = len(isConnected)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x: int, y: int) -> None:
            parent[find(x)] = find(y)

        # Union connected cities
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        # Count unique parents (provinces)
        return sum(i == find(i) for i in range(n))
