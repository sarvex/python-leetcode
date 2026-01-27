class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        """Enumerate valid decimal placements for both coordinates.

        Intuition:
            Split the string into two parts for x and y coordinates, then
            enumerate all valid decimal point placements for each part.

        Approach:
            1. For each split position, generate valid numbers for left and right parts.
            2. A number is valid if it has no leading zeros (unless "0" or "0.xxx")
               and no trailing zeros after the decimal point.
            3. Combine all valid (x, y) pairs.

        Complexity:
            Time: O(n^3) where n = len(s)
            Space: O(n^3) for storing results
        """

        def valid_numbers(start: int, end: int) -> list[str]:
            candidates: list[str] = []
            for decimal_pos in range(1, end - start + 1):
                integer_part = s[start : start + decimal_pos]
                fractional_part = s[start + decimal_pos : end]
                is_valid = (
                    integer_part == "0" or not integer_part.startswith("0")
                ) and not fractional_part.endswith("0")
                if is_valid:
                    candidates.append(
                        integer_part
                        + ("." if decimal_pos < end - start else "")
                        + fractional_part
                    )
            return candidates

        length = len(s)
        return [
            f"({x}, {y})"
            for split in range(2, length - 1)
            for x in valid_numbers(1, split)
            for y in valid_numbers(split, length - 1)
        ]
