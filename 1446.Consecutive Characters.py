from itertools import pairwise


class Solution:
    def maxPower(self, s: str) -> int:
        """Find the length of the longest substring of one repeating character.

        Intuition:
            Track the current run length of consecutive identical characters
            and record the maximum.

        Approach:
            Iterate through consecutive pairs. When characters match, extend
            the current streak; otherwise reset. Track the maximum streak.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        result = streak = 1
        for prev_char, curr_char in pairwise(s):
            if prev_char == curr_char:
                streak += 1
                result = max(result, streak)
            else:
                streak = 1
        return result
