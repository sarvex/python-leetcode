from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """Find the added character using frequency counting.

        Intuition:
            Since t is s with one extra character shuffled in, counting
            frequencies of s and decrementing for t reveals the added char.

        Approach:
            1. Count character frequencies in s.
            2. Iterate through t, decrementing counts.
            3. The first character whose count goes negative is the answer.

        Complexity:
            Time: O(n)
            Space: O(1) since alphabet size is fixed at 26
        """
        frequency = Counter(s)
        for char in t:
            frequency[char] -= 1
            if frequency[char] < 0:
                return char
