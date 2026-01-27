from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """Count k-length substrings with all unique characters using sliding window.

        Intuition:
            A sliding window of size k lets us efficiently track character
            frequencies and check for uniqueness as we slide across the string.

        Approach:
            Initialize a Counter for the first k characters. Slide the window
            one character at a time, adding the new character and removing the
            old one. Count windows where all characters are distinct (counter
            size equals k).

        Complexity:
            Time: O(n) where n is the length of s
            Space: O(k) for the character counter
        """
        char_count = Counter(s[:k])
        result = int(len(char_count) == k)
        for i in range(k, len(s)):
            char_count[s[i]] += 1
            char_count[s[i - k]] -= 1
            if char_count[s[i - k]] == 0:
                char_count.pop(s[i - k])
            result += int(len(char_count) == k)
        return result
