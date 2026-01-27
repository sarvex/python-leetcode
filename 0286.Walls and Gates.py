from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """Multi-source BFS from all gates simultaneously.

        Intuition:
            Starting BFS from all gates at once ensures each empty room is
            reached by the nearest gate first, giving the shortest distance
            in a single traversal.

        Approach:
            1. Collect all gate positions (value 0) into a queue.
            2. Perform BFS layer by layer, incrementing distance each level.
            3. For each neighbor that is an empty room (value 2^31-1), set its
               distance and add it to the queue.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(rooms), len(rooms[0])
        empty_room = 2**31 - 1
        queue = deque(
            (i, j) for i in range(rows) for j in range(cols) if rooms[i][j] == 0
        )
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for delta_row, delta_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    next_row, next_col = row + delta_row, col + delta_col
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and rooms[next_row][next_col] == empty_room
                    ):
                        rooms[next_row][next_col] = distance
                        queue.append((next_row, next_col))
