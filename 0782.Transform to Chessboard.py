class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        """Bitmask analysis of row/column patterns to determine minimum swaps.

        Intuition:
            A valid chessboard has only two distinct row patterns (complements of
            each other) and similarly for columns. We can encode rows and columns
            as bitmasks and count the minimum swaps needed to reach an alternating
            pattern.

        Approach:
            1. Encode the first row and first column as bitmasks
            2. Verify all rows match either the first row or its complement
            3. Same verification for columns
            4. Count swaps needed for rows and columns independently using
               bit manipulation against alternating masks (0xAAAAAAAA / 0x55555555)

        Complexity:
            Time: O(n^2) to scan the board
            Space: O(1) using bitmask representation
        """

        def count_swaps(mask: int, same_count: int) -> int:
            ones = mask.bit_count()
            if size & 1:
                if abs(size - 2 * ones) != 1 or abs(size - 2 * same_count) != 1:
                    return -1
                if ones == size // 2:
                    return size // 2 - (mask & 0xAAAAAAAA).bit_count()
                return (size + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                if ones != size // 2 or same_count != size // 2:
                    return -1
                swaps_even = size // 2 - (mask & 0xAAAAAAAA).bit_count()
                swaps_odd = size // 2 - (mask & 0x55555555).bit_count()
                return min(swaps_even, swaps_odd)

        size = len(board)
        full_mask = (1 << size) - 1
        row_mask = col_mask = 0
        for i in range(size):
            row_mask |= board[0][i] << i
            col_mask |= board[i][0] << i
        rev_row_mask = full_mask ^ row_mask
        rev_col_mask = full_mask ^ col_mask
        same_row = same_col = 0
        for i in range(size):
            cur_row_mask = cur_col_mask = 0
            for j in range(size):
                cur_row_mask |= board[i][j] << j
                cur_col_mask |= board[j][i] << j
            if cur_row_mask not in (row_mask, rev_row_mask) or cur_col_mask not in (
                col_mask,
                rev_col_mask,
            ):
                return -1
            same_row += cur_row_mask == row_mask
            same_col += cur_col_mask == col_mask
        row_swaps = count_swaps(row_mask, same_row)
        col_swaps = count_swaps(col_mask, same_col)
        return -1 if row_swaps == -1 or col_swaps == -1 else row_swaps + col_swaps
