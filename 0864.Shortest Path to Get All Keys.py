from collections import deque
from itertools import pairwise


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        """BFS with bitmask state tracking collected keys.

        Intuition:
        Each key changes the accessible paths, so the state includes position
        and the set of collected keys (as a bitmask). BFS on this state space
        finds the shortest path to collect all keys.

        Approach:
        1. Find the starting position and count total keys
        2. BFS with state (row, col, keys_bitmask)
        3. When visiting a key, update the bitmask
        4. Skip walls and locked doors without the matching key
        5. Return steps when all keys are collected

        Complexity:
        Time: O(m * n * 2^k) where k is the number of keys
        Space: O(m * n * 2^k) for visited states
        """
        rows, cols = len(grid), len(grid[0])
        start_row, start_col = next(
            (row, col)
            for row in range(rows)
            for col in range(cols)
            if grid[row][col] == "@"
        )
        total_keys = sum(cell.islower() for row in grid for cell in row)
        directions = (-1, 0, 1, 0, -1)
        queue: deque[tuple[int, int, int]] = deque([(start_row, start_col, 0)])
        visited: set[tuple[int, int, int]] = {(start_row, start_col, 0)}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col, key_state = queue.popleft()
                if key_state == (1 << total_keys) - 1:
                    return steps
                for delta_row, delta_col in pairwise(directions):
                    new_row, new_col = row + delta_row, col + delta_col
                    next_state = key_state
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        cell = grid[new_row][new_col]
                        if (
                            cell == "#"
                            or cell.isupper()
                            and (key_state & (1 << (ord(cell) - ord("A")))) == 0
                        ):
                            continue
                        if cell.islower():
                            next_state |= 1 << (ord(cell) - ord("a"))
                        if (new_row, new_col, next_state) not in visited:
                            visited.add((new_row, new_col, next_state))
                            queue.append((new_row, new_col, next_state))
            steps += 1
        return -1
