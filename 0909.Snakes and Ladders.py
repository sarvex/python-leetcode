from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """BFS to find shortest path on Boustrophedon board.

        Intuition:
            This is a shortest path problem on an unweighted graph. BFS gives
            the minimum number of dice rolls to reach the final square.

        Approach:
            1. Start BFS from square 1.
            2. For each square, try all dice rolls (1-6).
            3. Convert square number to board coordinates accounting for the
               alternating row direction (Boustrophedon order).
            4. Follow any snake or ladder at the destination.
            5. Return the number of moves when reaching square n*n.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        size = len(board)
        queue = deque([1])
        visited: set[int] = {1}
        moves = 0
        total_squares = size * size
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == total_squares:
                    return moves
                for next_sq in range(current + 1, min(current + 6, total_squares) + 1):
                    row, col = divmod(next_sq - 1, size)
                    if row & 1:
                        col = size - col - 1
                    row = size - row - 1
                    destination = next_sq if board[row][col] == -1 else board[row][col]
                    if destination not in visited:
                        visited.add(destination)
                        queue.append(destination)
            moves += 1
        return -1
