from math import inf


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """Find the longest substring where every vowel appears an even number of times.

        Intuition:
            Use a bitmask to track the parity of each vowel's count. A
            substring has all vowels in even counts when its start and end
            positions share the same bitmask state.

        Approach:
            Maintain a 5-bit state where each bit represents the parity of
            one vowel. Record the first occurrence of each state. The longest
            valid substring ending at position i has length i minus the first
            occurrence of the current state.

        Complexity:
            Time: O(n)
            Space: O(1) since there are at most 32 states.
        """
        first_occurrence = [inf] * 32
        first_occurrence[0] = -1
        vowels = "aeiou"
        state = 0
        result = 0

        for i, char in enumerate(s):
            for bit, vowel in enumerate(vowels):
                if char == vowel:
                    state ^= 1 << bit
            result = max(result, i - first_occurrence[state])
            first_occurrence[state] = min(first_occurrence[state], i)

        return result
