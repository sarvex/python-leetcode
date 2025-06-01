class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Two-pointer approach to find the length of the last word in a string.

        Intuition:
        Start from the end of the string and skip trailing spaces, then count
        characters until we hit another space or the beginning of the string.

        Approach:
        1. Start from the end of the string and skip all trailing spaces
        2. From the last non-space character, count backwards until we hit a space
        3. Return the difference between these two positions

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(1) as we only use two pointers
        """
        # Skip trailing spaces
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Find the beginning of the last word
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1

        return i - j
