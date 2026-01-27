from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """Find maximum instances of 'balloon' from characters in text.

        Intuition:
            The word 'balloon' requires specific character frequencies. The
            bottleneck is the character with the least available copies relative
            to its requirement.

        Approach:
            Count character frequencies in text. Since 'balloon' has two 'l's
            and two 'o's, halve those counts. Return the minimum count among
            the required characters.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        char_count = Counter(text)
        char_count["o"] >>= 1
        char_count["l"] >>= 1
        return min(char_count[ch] for ch in "balon")
