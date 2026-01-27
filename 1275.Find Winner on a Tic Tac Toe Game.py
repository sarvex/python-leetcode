class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        """Determine the winner of a tic-tac-toe game given the move sequence.

        Intuition:
            Track counts for each row, column, and both diagonals. A player
            wins when any count reaches 3. Since players alternate, check
            moves in reverse for the most recent player first.

        Approach:
            Use an array of 8 counters (3 rows + 3 columns + 2 diagonals).
            Iterate moves in reverse with step 2 to process one player at a
            time. Increment relevant counters and check for a win condition.

        Complexity:
            Time: O(n) where n is the number of moves
            Space: O(1)
        """
        move_count = len(moves)
        counters = [0] * 8
        for k in range(move_count - 1, -1, -2):
            row, col = moves[k]
            counters[row] += 1
            counters[col + 3] += 1
            if row == col:
                counters[6] += 1
            if row + col == 2:
                counters[7] += 1
            if any(v == 3 for v in counters):
                return "B" if k & 1 else "A"
        return "Draw" if move_count == 9 else "Pending"
