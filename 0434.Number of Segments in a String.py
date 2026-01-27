class Solution:
    def countSegments(self, text: str) -> int:
        """Split on whitespace and count non-empty segments.

        Intuition:
            Python's split() with no arguments splits on any whitespace and
            discards empty strings, giving exactly the segment count.

        Approach:
            1. Call split() on the string to split by whitespace.
            2. Return the length of the resulting list.

        Complexity:
            Time: O(n) where n is the length of the string.
            Space: O(n) for the split result.
        """
        return len(text.split())
