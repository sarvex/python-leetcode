from collections import defaultdict


class TicTacToe:
    """Tic-Tac-Toe game tracker using line counters.

    Intuition:
        Instead of storing the full board, track how many marks each player
        has placed on each row, column, and diagonal. A win occurs when any
        line reaches the board size.

    Approach:
        Maintain a counter dictionary per player. Each move increments the
        counts for the corresponding row, column, and (if applicable) the
        main diagonal and anti-diagonal. After updating, check whether any
        of the four relevant counters equals the board size.

    Complexity:
        Time: O(1) per move
        Space: O(n) for row, column, and diagonal counters
    """

    def __init__(self, n: int) -> None:
        """Initialize counters for an n x n board."""
        self.size = n
        self.counters = [defaultdict(int), defaultdict(int)]

    def move(self, row: int, col: int, player: int) -> int:
        """Place a mark and return the winning player (0 if no winner yet)."""
        current = self.counters[player - 1]
        size = self.size
        current[row] += 1
        current[size + col] += 1
        if row == col:
            current[size << 1] += 1
        if row + col == size - 1:
            current[size << 1 | 1] += 1
        if any(
            current[key] == size for key in (row, size + col, size << 1, size << 1 | 1)
        ):
            return player
        return 0
