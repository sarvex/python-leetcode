from collections import deque
from math import inf


class Solution:
    def findShortestWay(
        self, maze: list[list[int]], ball: list[int], hole: list[int]
    ) -> str:
        """BFS with lexicographic path tracking to find shortest path to hole.

        Intuition:
            The ball rolls until hitting a wall or the hole. We need the shortest
            path, and among equal-length paths, the lexicographically smallest
            instruction string.

        Approach:
            Use BFS where each state is a position the ball stops at. Track both
            distance and path string. Update a cell if we find a shorter distance
            or same distance with a lexicographically smaller path.

        Complexity:
            Time: O(m * n * max(m, n))
            Space: O(m * n)
        """
        rows, cols = len(maze), len(maze[0])
        row_ball, col_ball = ball
        row_hole, col_hole = hole
        queue = deque([(row_ball, col_ball)])
        dist = [[inf] * cols for _ in range(rows)]
        dist[row_ball][col_ball] = 0
        path = [[None] * cols for _ in range(rows)]
        path[row_ball][col_ball] = ""
        while queue:
            i, j = queue.popleft()
            for delta_row, delta_col, direction in [
                (-1, 0, "u"),
                (1, 0, "d"),
                (0, -1, "l"),
                (0, 1, "r"),
            ]:
                x, y, steps = i, j, dist[i][j]
                while (
                    0 <= x + delta_row < rows
                    and 0 <= y + delta_col < cols
                    and maze[x + delta_row][y + delta_col] == 0
                    and (x != row_hole or y != col_hole)
                ):
                    x, y = x + delta_row, y + delta_col
                    steps += 1
                if dist[x][y] > steps or (
                    dist[x][y] == steps and path[i][j] + direction < path[x][y]
                ):
                    dist[x][y] = steps
                    path[x][y] = path[i][j] + direction
                    if x != row_hole or y != col_hole:
                        queue.append((x, y))
        return path[row_hole][col_hole] or "impossible"
