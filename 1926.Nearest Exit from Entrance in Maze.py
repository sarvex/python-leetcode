from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """BFS with optimized exit checking for shortest path to exit

        Intuition:
        BFS guarantees the shortest path by exploring cells level by level.
        We can optimize by checking if a cell is an exit during enqueue rather than dequeue.

        Approach:
        1. Start BFS from entrance, marking it as visited
        2. Process cells level by level, tracking steps
        3. Check for exit condition when exploring neighbors
        4. Use in-place modification to track visited cells

        Complexity:
        Time: O(m*n) where m and n are the dimensions of the maze
        Space: O(m*n) for the queue in worst case
        """
        m, n = len(maze), len(maze[0])
        start_row, start_col = entrance

        # Early exit if entrance is invalid
        if start_row < 0 or start_row >= m or start_col < 0 or start_col >= n or maze[start_row][start_col] == '+':
            return -1

        # Initialize queue with entrance and mark as visited
        queue = deque([(start_row, start_col, 0)])
        maze[start_row][start_col] = '+'

        # Four directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            row, col, steps = queue.popleft()

            # Check all four adjacent cells
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc

                # Skip if out of bounds or wall/visited
                if nr < 0 or nr >= m or nc < 0 or nc >= n or maze[nr][nc] == '+':
                    continue

                # Check if this is an exit (border cell that's not the entrance)
                if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                    return steps + 1

                # Mark as visited and enqueue
                maze[nr][nc] = '+'
                queue.append((nr, nc, steps + 1))

        return -1
