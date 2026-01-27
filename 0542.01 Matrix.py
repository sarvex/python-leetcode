from collections import deque
from itertools import pairwise


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        """Multi-source BFS from all zero cells to compute nearest zero distances.

        Intuition:
            Start BFS from all zero cells simultaneously. Each cell's distance
            is determined by the first time it is reached.

        Approach:
            Initialize a distance matrix with -1. Enqueue all zero cells with
            distance 0. BFS outward, setting distance for unvisited cells.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(mat), len(mat[0])
        distances = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for i, row in enumerate(mat):
            for j, value in enumerate(row):
                if value == 0:
                    distances[i][j] = 0
                    queue.append((i, j))
        dirs = (-1, 0, 1, 0, -1)
        while queue:
            i, j = queue.popleft()
            for delta_row, delta_col in pairwise(dirs):
                x, y = i + delta_row, j + delta_col
                if 0 <= x < rows and 0 <= y < cols and distances[x][y] == -1:
                    distances[x][y] = distances[i][j] + 1
                    queue.append((x, y))
        return distances
