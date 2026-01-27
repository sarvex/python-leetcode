from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """Greedy character pairing for longest palindrome length.

        Intuition:
            A palindrome uses characters in pairs. Any character with an
            even count contributes fully. We can also place one odd-count
            character in the center.

        Approach:
            1. Count character frequencies.
            2. Sum up the largest even portion of each count (v // 2 * 2).
            3. If the total is less than the string length, at least one
               character has an odd count and we can add 1 for the center.

        Complexity:
            Time: O(n)
            Space: O(1) since alphabet size is bounded
        """
        frequency = Counter(s)
        paired_length = sum(count // 2 * 2 for count in frequency.values())
        paired_length += int(paired_length < len(s))
        return paired_length
