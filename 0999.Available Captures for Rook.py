from itertools import pairwise


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        """Count the number of pawns a rook can capture on a chess board.

        Intuition:
            Find the rook then scan in all four cardinal directions. A pawn is
            capturable if no bishop blocks the path.

        Approach:
            Locate the rook, then for each direction walk until reaching a pawn
            (count it) or a bishop (stop). Use a direction array for conciseness.

        Complexity:
            Time: O(64) constant since the board is always 8×8
            Space: O(1)
        """
        captures = 0
        directions = (-1, 0, 1, 0, -1)
        for row in range(8):
            for col in range(8):
                if board[row][col] == "R":
                    for delta_row, delta_col in pairwise(directions):
                        r, c = row, col
                        while 0 <= r + delta_row < 8 and 0 <= c + delta_col < 8:
                            r, c = r + delta_row, c + delta_col
                            if board[r][c] == "p":
                                captures += 1
                                break
                            if board[r][c] == "B":
                                break
        return captures
