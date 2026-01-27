class Solution:
    def reverseString(self, s: list[str]) -> None:
        """Two-pointer in-place string reversal.

        Intuition:
            Swap characters from both ends moving toward the center.

        Approach:
            1. Initialize two pointers at the start and end of the list.
            2. Swap elements at both pointers and move them inward.
            3. Stop when the pointers meet.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
