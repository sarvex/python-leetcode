from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        """Shortest path in grid with at most k obstacle eliminations.

        Intuition:
            BFS over states (row, col, remaining_eliminations) finds the shortest
            path. If k is large enough, the Manhattan distance is the answer.

        Approach:
            Use BFS with state (row, col, remaining_k). Early exit if k >= m+n-3
            since we can walk the Manhattan path. Track visited states to avoid
            revisiting with the same or fewer remaining eliminations.

        Complexity:
            Time: O(m * n * k)
            Space: O(m * n * k)
        """
        rows, cols = len(grid), len(grid[0])
        if k >= rows + cols - 3:
            return rows + cols - 2

        queue = deque([(0, 0, k)])
        visited: set[tuple[int, int, int]] = {(0, 0, k)}
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                row, col, remaining = queue.popleft()
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row, next_col = row + delta_row, col + delta_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if next_row == rows - 1 and next_col == cols - 1:
                            return steps
                        if (
                            grid[next_row][next_col] == 0
                            and (next_row, next_col, remaining) not in visited
                        ):
                            queue.append((next_row, next_col, remaining))
                            visited.add((next_row, next_col, remaining))
                        if (
                            grid[next_row][next_col] == 1
                            and remaining > 0
                            and (next_row, next_col, remaining - 1) not in visited
                        ):
                            queue.append((next_row, next_col, remaining - 1))
                            visited.add((next_row, next_col, remaining - 1))
        return -1
