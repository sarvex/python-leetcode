from typing import List, Set, Deque
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        BFS traversal to check if all rooms can be visited

        Intuition:
        We can model this problem as a graph traversal where each room is a node
        and keys are directed edges to other rooms. If we can reach all rooms
        starting from room 0, then we can visit all rooms.

        Approach:
        1. Use BFS to traverse through all accessible rooms starting from room 0
        2. Keep track of visited rooms in a set
        3. After traversal, check if the number of visited rooms equals the total number of rooms

        Complexity:
        Time: O(n + k) where n is the number of rooms and k is the total number of keys
        Space: O(n) for the visited set and queue
        """
        # Iterative BFS approach (more memory efficient for large inputs)
        visited: Set[int] = set()
        queue: Deque[int] = deque([0])  # Start with room 0

        while queue:
            room = queue.popleft()
            if room in visited:
                continue

            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)

        return len(visited) == len(rooms)

    def canVisitAllRooms_dfs(self, rooms: List[List[int]]) -> bool:
        """
        DFS traversal to check if all rooms can be visited

        Complexity:
        Time: O(n + k) where n is the number of rooms and k is the total number of keys
        Space: O(n) for the visited set and recursion stack
        """
        def dfs(room: int, visited: Set[int]) -> None:
            """Visit a room and explore all rooms accessible from its keys"""
            if room in visited:
                return

            visited.add(room)
            for key in rooms[room]:
                dfs(key, visited)

        visited: Set[int] = set()
        dfs(0, visited)
        return len(visited) == len(rooms)
