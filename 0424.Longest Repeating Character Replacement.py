from collections import Counter


class Solution:
    def characterReplacement(self, text: str, max_replacements: int) -> int:
        """Sliding window tracking the most frequent character in the window.

        Intuition:
            The longest valid substring has at most k characters that differ from
            the most frequent character. Expand the window and shrink when the
            number of replacements exceeds k.

        Approach:
            1. Use a sliding window with left and right pointers.
            2. Track character frequencies and the maximum frequency in the window.
            3. If window_size - max_frequency > k, shrink the window from the left.
            4. The answer is the total length minus the final left pointer.

        Complexity:
            Time: O(n) where n is the length of the string.
            Space: O(26) = O(1) for the character counter.
        """
        frequency = Counter()
        left = max_freq = 0
        for right, char in enumerate(text):
            frequency[char] += 1
            max_freq = max(max_freq, frequency[char])
            if right - left + 1 - max_freq > max_replacements:
                frequency[text[left]] -= 1
                left += 1
        return len(text) - left
