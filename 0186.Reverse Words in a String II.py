class Solution:
    def reverseWords(self, s: list[str]) -> None:
        """Two-Pass Reverse Approach

        Intuition:
            Reverse each word individually, then reverse the entire string
            to achieve word-level reversal in place.

        Approach:
            1. Iterate through the list to find word boundaries (spaces).
            2. Reverse each word in place using two pointers.
            3. After processing all words, reverse the entire list.

        Complexity:
            Time: O(n) where n is the length of the character list
            Space: O(1) in-place reversal
        """

        def reverse(left: int, right: int) -> None:
            while left < right:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1

        word_start, length = 0, len(s)
        for idx, char in enumerate(s):
            if char == " ":
                reverse(word_start, idx - 1)
                word_start = idx + 1
            elif idx == length - 1:
                reverse(word_start, idx)
        reverse(0, length - 1)
