from collections import deque


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        """Minimum moves to reach target with rotations using BFS.

        Intuition:
            Model the snake as two cells and use BFS to explore all possible
            moves (slide right, slide down, rotate clockwise/counterclockwise).

        Approach:
            Represent state as (head_flat_index, status) where status is 0 for
            horizontal and 1 for vertical. BFS explores sliding and rotation
            moves, checking grid boundaries and obstacles.

        Complexity:
            Time: O(n^2) where n is the grid dimension
            Space: O(n^2) for the visited set and queue
        """

        def try_move(row1: int, col1: int, row2: int, col2: int) -> None:
            if (
                0 <= row1 < size
                and 0 <= col1 < size
                and 0 <= row2 < size
                and 0 <= col2 < size
            ):
                flat = row1 * size + col1
                status = 0 if row1 == row2 else 1
                if (
                    (flat, status) not in visited
                    and grid[row1][col1] == 0
                    and grid[row2][col2] == 0
                ):
                    queue.append((flat, row2 * size + col2))
                    visited.add((flat, status))

        size = len(grid)
        target = (size * size - 2, size * size - 1)
        queue: deque[tuple[int, int]] = deque([(0, 1)])
        visited: set[tuple[int, int]] = {(0, 0)}
        moves = 0
        while queue:
            for _ in range(len(queue)):
                head, tail = queue.popleft()
                if (head, tail) == target:
                    return moves
                row1, col1 = divmod(head, size)
                row2, col2 = divmod(tail, size)
                try_move(row1, col1 + 1, row2, col2 + 1)
                try_move(row1 + 1, col1, row2 + 1, col2)
                if row1 == row2 and row1 + 1 < size and grid[row1 + 1][col2] == 0:
                    try_move(row1, col1, row1 + 1, col1)
                if col1 == col2 and col1 + 1 < size and grid[row2][col1 + 1] == 0:
                    try_move(row1, col1, row1, col1 + 1)
            moves += 1
        return -1
