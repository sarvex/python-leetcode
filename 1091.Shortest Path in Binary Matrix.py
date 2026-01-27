from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """Find shortest path from top-left to bottom-right in binary matrix.

        Intuition:
            BFS gives the shortest path in an unweighted grid, exploring all
            8 directions at each cell.

        Approach:
            Start BFS from (0,0). Mark visited cells by setting them to 1.
            Expand level by level, checking all 8 neighbors. Return distance
            when reaching (n-1, n-1).

        Complexity:
            Time: O(n^2)
            Space: O(n^2) for the BFS queue
        """
        if grid[0][0]:
            return -1
        n = len(grid)
        grid[0][0] = 1
        queue = deque([(0, 0)])
        distance = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == col == n - 1:
                    return distance
                for next_row in range(row - 1, row + 2):
                    for next_col in range(col - 1, col + 2):
                        if (
                            0 <= next_row < n
                            and 0 <= next_col < n
                            and grid[next_row][next_col] == 0
                        ):
                            grid[next_row][next_col] = 1
                            queue.append((next_row, next_col))
            distance += 1
        return -1
