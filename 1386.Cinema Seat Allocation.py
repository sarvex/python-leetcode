from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """Bit manipulation for optimal cinema seat allocation

        Intuition:
        Use bit manipulation to represent seat reservations and efficiently check if
        groups of 4 adjacent seats are available in each row.

        Approach:
        1. Map each row to a bitmask where 1 means the seat is reserved
        2. Define three possible seating arrangements (left, middle, right)
        3. For empty rows, we can fit 2 families
        4. For rows with reservations, check each possible arrangement

        Complexity:
        Time: O(m) where m is the number of reserved seats
        Space: O(m) for storing the row reservations
        """
        # Map each row to a bitmask of reserved seats
        reserved_rows = defaultdict(int)

        # Create bitmasks for each row
        for row, seat in reservedSeats:
            reserved_rows[row] |= 1 << (10 - seat)

        # Define the three possible seating arrangements as bitmasks
        # Seats 2-5 (left), 6-9 (right), and 4-7 (middle)
        masks = (0b0111100000,  # Seats 2-5 (left)
                0b0000011110,  # Seats 6-9 (right)
                0b0001111000)  # Seats 4-7 (middle)

        # Each empty row can fit 2 families
        total_families = (n - len(reserved_rows)) * 2

        # Process rows with reservations
        for row_mask in reserved_rows.values():
            families_in_row = 0
            for mask in masks:
                if (row_mask & mask) == 0:  # If seats are available
                    row_mask |= mask  # Mark as used
                    families_in_row += 1
                    # Maximum 2 families per row
                    if families_in_row == 2:
                        break
            total_families += families_in_row

        return total_families
