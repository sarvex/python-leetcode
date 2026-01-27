class Solution:
    def queensAttacktheKing(
        self, queens: list[list[int]], king: list[int]
    ) -> list[list[int]]:
        """Queens that can attack the king on a chessboard.

        Intuition:
            From the king's position, search outward in all 8 directions. The
            first queen found in each direction can attack the king.

        Approach:
            Store queen positions in a set for O(1) lookup. For each of the
            8 directions, walk outward from the king until finding a queen or
            going out of bounds.

        Complexity:
            Time: O(1) since the board is fixed 8x8
            Space: O(q) where q is the number of queens
        """
        board_size = 8
        queen_set = {(row, col) for row, col in queens}
        result: list[list[int]] = []
        for delta_row in range(-1, 2):
            for delta_col in range(-1, 2):
                if delta_row or delta_col:
                    row, col = king[0], king[1]
                    while (
                        0 <= row + delta_row < board_size
                        and 0 <= col + delta_col < board_size
                    ):
                        row += delta_row
                        col += delta_col
                        if (row, col) in queen_set:
                            result.append([row, col])
                            break
        return result
