from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """Binary search for the first letter strictly greater than target.

        Intuition:
            The sorted letter list allows binary search to efficiently locate
            the insertion point just past the target character.

        Approach:
            1. Use bisect_right with an ord-based key to find the first letter
               greater than target.
            2. Wrap around using modulo if target is >= all letters.

        Complexity:
            Time: O(log N)
            Space: O(1)
        """
        index = bisect_right(letters, ord(target), key=lambda c: ord(c))
        return letters[index % len(letters)]
