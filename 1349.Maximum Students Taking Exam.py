from functools import cache


class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        """Find maximum students that can sit without cheating.

        Intuition:
            Use bitmask DP on rows. Each row's seating is a bitmask of occupied
            seats. Valid masks have no adjacent students and no diagonal neighbors
            from the previous row.

        Approach:
            Convert each row to an availability bitmask. For each row, enumerate
            valid seating masks (subset of available, no adjacent bits). Use
            cached recursion, propagating constraints to the next row by masking
            out diagonal positions.

        Complexity:
            Time: O(m * 2^n * 2^n) where m is rows, n is columns
            Space: O(m * 2^n)
        """
        num_cols = len(seats[0])
        availability = [self._row_to_mask(row) for row in seats]

        @cache
        def search(available: int, row: int) -> int:
            best = 0
            for mask in range(1 << num_cols):
                if (available | mask) != available or (mask & (mask << 1)):
                    continue
                student_count = mask.bit_count()
                if row == len(availability) - 1:
                    best = max(best, student_count)
                else:
                    next_available = availability[row + 1]
                    next_available &= ~(mask << 1)
                    next_available &= ~(mask >> 1)
                    best = max(best, student_count + search(next_available, row + 1))
            return best

        return search(availability[0], 0)

    @staticmethod
    def _row_to_mask(row: list[str]) -> int:
        mask = 0
        for i, cell in enumerate(row):
            if cell == ".":
                mask |= 1 << i
        return mask
