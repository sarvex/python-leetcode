class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """Two-pointer validation using strobogrammatic digit mapping.

        Intuition:
            A strobogrammatic number reads the same upside down. Only digits
            0, 1, 6, 8, 9 have valid rotations. Use a lookup to verify pairs
            from both ends.

        Approach:
            Build a rotation map where each digit maps to its rotated form
            (-1 for invalid). Use two pointers from both ends, checking that
            each digit pair satisfies the rotation relationship.

        Complexity:
            Time: O(n) where n is the length of num
            Space: O(1)
        """
        rotation_map = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        left, right = 0, len(num) - 1
        while left <= right:
            left_digit, right_digit = int(num[left]), int(num[right])
            if rotation_map[left_digit] != right_digit:
                return False
            left, right = left + 1, right - 1
        return True
