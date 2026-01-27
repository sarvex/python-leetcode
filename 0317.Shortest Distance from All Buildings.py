from collections import deque
from math import inf


class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        """Multi-source BFS from each building to compute total distances.

        Intuition:
            BFS from every building to compute the distance to all reachable
            empty cells. The answer is the empty cell reachable by all buildings
            with the minimum total distance.

        Approach:
            1. For each building, run BFS to compute distances to all empty cells.
            2. Accumulate distances and reachability counts for each empty cell.
            3. Find the empty cell reachable by all buildings with minimum total distance.

        Complexity:
            Time: O(b * m * n) where b is number of buildings
            Space: O(m * n) for distance and count matrices
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        building_count = 0
        reach_count = [[0] * cols for _ in range(rows)]
        total_dist = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    building_count += 1
                    queue.append((i, j))
                    distance = 0
                    visited: set[tuple[int, int]] = set()
                    while queue:
                        distance += 1
                        for _ in range(len(queue)):
                            row, col = queue.popleft()
                            for delta_row, delta_col in [
                                [0, 1],
                                [0, -1],
                                [1, 0],
                                [-1, 0],
                            ]:
                                next_row, next_col = row + delta_row, col + delta_col
                                if (
                                    0 <= next_row < rows
                                    and 0 <= next_col < cols
                                    and grid[next_row][next_col] == 0
                                    and (next_row, next_col) not in visited
                                ):
                                    reach_count[next_row][next_col] += 1
                                    total_dist[next_row][next_col] += distance
                                    queue.append((next_row, next_col))
                                    visited.add((next_row, next_col))
        min_distance = inf
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and reach_count[i][j] == building_count:
                    min_distance = min(min_distance, total_dist[i][j])
        return -1 if min_distance == inf else min_distance
