from math import inf


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        """Two-pass sweep to find nearest occurrence from left and right.

        Intuition:
            Sweep left-to-right tracking the last seen position of c, then
            right-to-left tracking the next seen position. Take the minimum.

        Approach:
            1. Forward pass: for each position, compute distance to the last
               occurrence of c to its left.
            2. Backward pass: compute distance to the next occurrence to its right.
            3. Take the minimum of both passes.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(s)
        distances = [length] * length
        prev_occurrence = -inf
        for i, char in enumerate(s):
            if char == c:
                prev_occurrence = i
            distances[i] = min(distances[i], i - prev_occurrence)
        next_occurrence = inf
        for i in range(length - 1, -1, -1):
            if s[i] == c:
                next_occurrence = i
            distances[i] = min(distances[i], next_occurrence - i)
        return distances
