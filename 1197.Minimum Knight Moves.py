from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """Minimum knight moves to reach (x, y) from origin using BFS.

        Intuition:
            BFS from the origin explores positions level by level, guaranteeing
            the shortest path in an unweighted graph.

        Approach:
            Use BFS starting from (0, 0) with all 8 knight move directions.
            Track visited positions to avoid revisiting. Return the level count
            when the target is reached.

        Complexity:
            Time: O(|x| * |y|) bounded by the search space
            Space: O(|x| * |y|)
        """
        queue: deque[tuple[int, int]] = deque([(0, 0)])
        moves = 0
        visited: set[tuple[int, int]] = {(0, 0)}
        knight_offsets = (
            (-2, 1),
            (-1, 2),
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
        )
        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == (x, y):
                    return moves
                for dx, dy in knight_offsets:
                    next_x, next_y = curr_x + dx, curr_y + dy
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))
            moves += 1
        return -1
