class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """Compare two strings for longest uncommon subsequence.

        Intuition:
            If the strings are different, the longer one is always an uncommon
            subsequence. If they are identical, no uncommon subsequence exists.

        Approach:
            Return -1 if strings are equal, otherwise return the length of
            the longer string.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return -1 if a == b else max(len(a), len(b))
