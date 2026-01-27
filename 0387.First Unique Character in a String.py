from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Find first non-repeating character using frequency counting.

        Intuition:
            Count character frequencies first, then scan left to right
            to find the first character with count 1.

        Approach:
            1. Build a frequency counter for all characters.
            2. Iterate through the string with index.
            3. Return the first index where the character count is 1.

        Complexity:
            Time: O(n)
            Space: O(1) since alphabet size is fixed at 26
        """
        frequency = Counter(s)
        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i
        return -1
