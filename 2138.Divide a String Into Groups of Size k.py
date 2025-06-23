from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Divide a string into groups of size k with fill character for the last group.

        Intuition:
        Iterate through the string with steps of size k and create substrings.
        For the last group, if it's not of size k, fill it with the provided character.

        Approach:
        1. Use list comprehension to create substrings of length k
        2. Use string's ljust method to pad the last group if needed
        3. Return the list of substrings

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(n) for storing the result
        """
        return [s[i:i + k].ljust(k, fill) for i in range(0, len(s), k)]
