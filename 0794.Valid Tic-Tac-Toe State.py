class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        """Validate tic-tac-toe board state by counting moves and wins.

        Intuition:
            A valid board must have X count equal to or one more than O count,
            and both players cannot have won simultaneously.

        Approach:
            1. Count X and O pieces; X must equal O or O+1.
            2. Check if X wins — if so, X must have moved last (x_count == o_count + 1).
            3. Check if O wins — if so, O must have moved last (x_count == o_count).

        Complexity:
            Time: O(1) — board is always 3x3
            Space: O(1)
        """

        def has_won(player: str) -> bool:
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)):
                return True
            return all(board[i][2 - i] == player for i in range(3))

        x_count = sum(board[i][j] == "X" for i in range(3) for j in range(3))
        o_count = sum(board[i][j] == "O" for i in range(3) for j in range(3))
        if x_count != o_count and x_count - 1 != o_count:
            return False
        if has_won("X") and x_count - 1 != o_count:
            return False
        return not (has_won("O") and x_count != o_count)
