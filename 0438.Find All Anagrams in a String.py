from collections import Counter


class Solution:
    def findAnagrams(self, text: str, pattern: str) -> list[int]:
        """Sliding window comparing character frequency counters.

        Intuition:
            A fixed-size window of length len(pattern) slides over text. If the
            window's character frequencies match pattern's, it's an anagram.

        Approach:
            1. Count pattern frequencies.
            2. Initialize a window counter with the first (n-1) characters.
            3. Slide the window: add the new right character, compare counters,
               then remove the leftmost character.
            4. Collect matching start indices.

        Complexity:
            Time: O(m) where m is the length of text (counter comparison is O(26)).
            Space: O(26) = O(1) for the character counters.
        """
        text_len, pattern_len = len(text), len(pattern)
        result: list[int] = []
        if text_len < pattern_len:
            return result
        pattern_count = Counter(pattern)
        window_count = Counter(text[: pattern_len - 1])
        for i in range(pattern_len - 1, text_len):
            window_count[text[i]] += 1
            if pattern_count == window_count:
                result.append(i - pattern_len + 1)
            window_count[text[i - pattern_len + 1]] -= 1
        return result
