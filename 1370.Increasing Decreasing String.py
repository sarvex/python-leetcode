from collections import Counter
from string import ascii_lowercase


class Solution:
    def sortString(self, s: str) -> str:
        """Build a string by alternately picking characters in increasing and decreasing order.

        Intuition:
            Repeatedly sweep through the alphabet forward then backward,
            picking available characters, until all are used.

        Approach:
            Count character frequencies. Alternate between ascending and
            descending sweeps through the alphabet, appending each available
            character and decrementing its count.

        Complexity:
            Time: O(n * 26) which simplifies to O(n).
            Space: O(n)
        """
        frequency = Counter(s)
        forward_backward = ascii_lowercase + ascii_lowercase[::-1]
        result: list[str] = []

        while len(result) < len(s):
            for char in forward_backward:
                if frequency[char]:
                    result.append(char)
                    frequency[char] -= 1

        return "".join(result)
