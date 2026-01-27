class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """Two-pointer comparison skipping X characters with position constraints.

        Intuition:
            L can only move left and R can only move right. After removing all X's,
            both strings must have the same sequence of L and R. Additionally, each
            L in start must be at or to the right of its corresponding L in end,
            and each R must be at or to the left.

        Approach:
            1. Use two pointers to skip X characters in both strings
            2. At each non-X position, verify characters match
            3. Check position constraints: L cannot move right, R cannot move left
            4. Both pointers must exhaust simultaneously

        Complexity:
            Time: O(n) where n is the string length
            Space: O(1)
        """
        length = len(start)
        start_idx = end_idx = 0
        while True:
            while start_idx < length and start[start_idx] == "X":
                start_idx += 1
            while end_idx < length and end[end_idx] == "X":
                end_idx += 1
            if start_idx >= length and end_idx >= length:
                return True
            if (
                start_idx >= length
                or end_idx >= length
                or start[start_idx] != end[end_idx]
            ):
                return False
            if start[start_idx] == "L" and start_idx < end_idx:
                return False
            if start[start_idx] == "R" and start_idx > end_idx:
                return False
            start_idx, end_idx = start_idx + 1, end_idx + 1
