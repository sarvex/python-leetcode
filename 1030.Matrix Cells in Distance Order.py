from collections import deque
from itertools import pairwise


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> list[list[int]]:
        """Matrix Cells in Distance Order via BFS from center.

        Intuition:
            BFS naturally explores cells in order of increasing Manhattan
            distance from the starting cell.

        Approach:
            Start BFS from (rCenter, cCenter). Use a visited matrix to avoid
            revisiting cells. Append each cell to the result as it is dequeued.

        Complexity:
            Time: O(rows * cols)
            Space: O(rows * cols)
        """
        queue = deque([[rCenter, cCenter]])
        visited = [[False] * cols for _ in range(rows)]
        visited[rCenter][cCenter] = True
        result: list[list[int]] = []
        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                result.append(cell)
                for delta_r, delta_c in pairwise((-1, 0, 1, 0, -1)):
                    next_row, next_col = cell[0] + delta_r, cell[1] + delta_c
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and not visited[next_row][next_col]
                    ):
                        visited[next_row][next_col] = True
                        queue.append([next_row, next_col])
        return result
