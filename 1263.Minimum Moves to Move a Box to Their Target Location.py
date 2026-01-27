from collections import deque
from itertools import pairwise


class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        """Find minimum pushes to move a box to the target on a grid.

        Intuition:
            This is a shortest path problem with two agents (player and box).
            Moving the player without pushing costs 0, pushing costs 1. A
            0-1 BFS handles this efficiently.

        Approach:
            Use 0-1 BFS on the state (player_position, box_position). Player
            moves that do not push the box have weight 0 (added to front of
            deque). Moves that push the box have weight 1 (added to back).
            Track visited states to avoid revisiting.

        Complexity:
            Time: O((m * n)^2)
            Space: O((m * n)^2)
        """

        def to_index(row: int, col: int) -> int:
            return row * cols + col

        def is_valid(row: int, col: int) -> bool:
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] != "#"

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "S":
                    start_row, start_col = i, j
                elif cell == "B":
                    box_row, box_col = i, j

        rows, cols = len(grid), len(grid[0])
        directions = (-1, 0, 1, 0, -1)
        queue = deque([(to_index(start_row, start_col), to_index(box_row, box_col), 0)])
        visited = [[False] * (rows * cols) for _ in range(rows * cols)]
        visited[to_index(start_row, start_col)][to_index(box_row, box_col)] = True

        while queue:
            player, box, pushes = queue.popleft()
            bi, bj = box // cols, box % cols
            if grid[bi][bj] == "T":
                return pushes
            si, sj = player // cols, player % cols
            for dr, dc in pairwise(directions):
                new_sr, new_sc = si + dr, sj + dc
                if not is_valid(new_sr, new_sc):
                    continue
                if new_sr == bi and new_sc == bj:
                    new_br, new_bc = bi + dr, bj + dc
                    if (
                        not is_valid(new_br, new_bc)
                        or visited[to_index(new_sr, new_sc)][to_index(new_br, new_bc)]
                    ):
                        continue
                    visited[to_index(new_sr, new_sc)][to_index(new_br, new_bc)] = True
                    queue.append(
                        (to_index(new_sr, new_sc), to_index(new_br, new_bc), pushes + 1)
                    )
                elif not visited[to_index(new_sr, new_sc)][to_index(bi, bj)]:
                    visited[to_index(new_sr, new_sc)][to_index(bi, bj)] = True
                    queue.appendleft(
                        (to_index(new_sr, new_sc), to_index(bi, bj), pushes)
                    )
        return -1
