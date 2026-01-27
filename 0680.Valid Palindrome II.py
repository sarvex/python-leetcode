class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Two-pointer palindrome check with at most one deletion.

        Intuition:
            Use two pointers from both ends. When a mismatch is found, try
            skipping either the left or right character and check if the
            remaining substring is a palindrome.

        Approach:
            1. Use two pointers moving inward from both ends.
            2. On mismatch, check if skipping one character from either side
               yields a palindrome.
            3. Use a helper function to verify palindrome for a given range.

        Complexity:
            Time: O(n) single pass with at most one additional check
            Space: O(1) only pointer variables
        """

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            left, right = left + 1, right - 1
        return True
