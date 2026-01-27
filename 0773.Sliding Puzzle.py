from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        """BFS over board states to find shortest path to goal configuration.

        Intuition:
            The sliding puzzle has a small fixed state space (6 tiles). BFS
            guarantees the shortest number of moves by exploring all states
            at each depth level before moving deeper.

        Approach:
            1. Encode the board as a string for efficient hashing
            2. Use BFS starting from the initial state
            3. At each step, find the zero tile, generate all neighbor states
               by swapping zero with adjacent tiles
            4. Track visited states to avoid cycles
            5. Return the depth when the goal state "123450" is reached

        Complexity:
            Time: O(6! * 6) — at most 720 states, each generating up to 4 neighbors
            Space: O(6!) for the visited set
        """
        tiles: list[str] = [""] * 6

        def get_state() -> str:
            for i in range(2):
                for j in range(3):
                    tiles[i * 3 + j] = str(board[i][j])
            return "".join(tiles)

        def set_board(state: str) -> None:
            for i in range(2):
                for j in range(3):
                    board[i][j] = int(state[i * 3 + j])

        def get_neighbors() -> list[str]:
            neighbors: list[str] = []
            row, col = next(
                (i, j) for i in range(2) for j in range(3) if board[i][j] == 0
            )
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + delta_row, col + delta_col
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    board[row][col], board[new_row][new_col] = (
                        board[new_row][new_col],
                        board[row][col],
                    )
                    neighbors.append(get_state())
                    board[row][col], board[new_row][new_col] = (
                        board[new_row][new_col],
                        board[row][col],
                    )
            return neighbors

        start = get_state()
        goal = "123450"
        if start == goal:
            return 0
        visited: set[str] = {start}
        queue = deque([start])
        moves = 0
        while queue:
            moves += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                set_board(current)
                for neighbor in get_neighbors():
                    if neighbor == goal:
                        return moves
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return -1
