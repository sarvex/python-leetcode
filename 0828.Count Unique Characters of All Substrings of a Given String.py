from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """Count contribution of each character across all substrings.

        Intuition:
            For each occurrence of a character, count the number of substrings
            where it is unique by considering the gap between consecutive
            occurrences of the same character.

        Approach:
            1. Record positions of each character.
            2. For each character, pad positions with -1 and len(s) as boundaries.
            3. Each occurrence at index positions[i] contributes
               (positions[i] - positions[i-1]) * (positions[i+1] - positions[i]) substrings.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        char_positions: defaultdict[str, list[int]] = defaultdict(list)
        for i, char in enumerate(s):
            char_positions[char].append(i)
        result = 0
        for positions in char_positions.values():
            positions = [-1] + positions + [len(s)]
            for i in range(1, len(positions) - 1):
                result += (positions[i] - positions[i - 1]) * (
                    positions[i + 1] - positions[i]
                )
        return result
