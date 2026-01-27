class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        """Count lines needed by tracking current line width.

        Intuition:
            Greedily fill each line up to 100 pixels, wrapping to a new line
            when a character would exceed the limit.

        Approach:
            1. For each character, look up its width from the widths array.
            2. If adding it exceeds 100, start a new line.
            3. Return the line count and last line width.

        Complexity:
            Time: O(n) where n = len(s)
            Space: O(1)
        """
        lines, current_width = 1, 0
        for char_width in (widths[ord(char) - ord("a")] for char in s):
            if current_width + char_width <= 100:
                current_width += char_width
            else:
                lines += 1
                current_width = char_width
        return [lines, current_width]
