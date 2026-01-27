from collections import deque
from itertools import pairwise
from math import inf


class Solution:
    def shortestDistance(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> int:
        """BFS to find shortest rolling distance in a maze.

        Intuition:
            The ball rolls until hitting a wall. We need to find the shortest
            distance from start to destination, where distance is the number
            of cells the ball passes through.

        Approach:
            Use BFS where each state is a resting position. For each position,
            roll in all four directions until hitting a wall, tracking distance.
            Update if a shorter path is found.

        Complexity:
            Time: O(m * n * max(m, n))
            Space: O(m * n)
        """
        rows, cols = len(maze), len(maze[0])
        dirs = (-1, 0, 1, 0, -1)
        start_row, start_col = start
        dest_row, dest_col = destination
        queue = deque([(start_row, start_col)])
        dist = [[inf] * cols for _ in range(rows)]
        dist[start_row][start_col] = 0
        while queue:
            i, j = queue.popleft()
            for delta_row, delta_col in pairwise(dirs):
                x, y, steps = i, j, dist[i][j]
                while (
                    0 <= x + delta_row < rows
                    and 0 <= y + delta_col < cols
                    and maze[x + delta_row][y + delta_col] == 0
                ):
                    x, y, steps = x + delta_row, y + delta_col, steps + 1
                if steps < dist[x][y]:
                    dist[x][y] = steps
                    queue.append((x, y))
        return -1 if dist[dest_row][dest_col] == inf else dist[dest_row][dest_col]
