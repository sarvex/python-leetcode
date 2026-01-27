from collections import deque


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        """Find minimum cost to make at least one valid path from top-left to bottom-right.

        Intuition:
            This is a shortest path problem where following the existing arrow
            costs 0 and changing direction costs 1. A 0-1 BFS handles this
            efficiently using a deque.

        Approach:
            Use 0-1 BFS with a deque. For each cell, moving in the direction
            the arrow already points has cost 0 (add to front), while any
            other direction has cost 1 (add to back). Track visited cells to
            avoid revisiting.

        Complexity:
            Time: O(m * n) where m and n are grid dimensions.
            Space: O(m * n)
        """
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        visited: set[tuple[int, int]] = set()

        while queue:
            row, col, cost = queue.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == rows - 1 and col == cols - 1:
                return cost
            for direction in range(1, 5):
                new_row = row + directions[direction][0]
                new_col = col + directions[direction][1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[row][col] == direction:
                        queue.appendleft((new_row, new_col, cost))
                    else:
                        queue.append((new_row, new_col, cost + 1))

        return -1
