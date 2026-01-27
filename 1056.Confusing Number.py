class Solution:
    def confusingNumber(self, n: int) -> bool:
        """Check if n becomes a different number when rotated 180 degrees.

        Intuition:
            Map each digit to its rotated counterpart and check if the reversed
            result differs from the original.

        Approach:
            Process digits right-to-left, mapping each through a rotation table.
            If any digit is invalid, return False. Compare rotated number to original.

        Complexity:
            Time: O(log n) for digit processing
            Space: O(1)
        """
        rotation_map = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        remaining, rotated = n, 0
        while remaining:
            remaining, digit = divmod(remaining, 10)
            if rotation_map[digit] < 0:
                return False
            rotated = rotated * 10 + rotation_map[digit]
        return rotated != n
