from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Character frequency comparison using Counter.

        Intuition:
            Two strings are anagrams if and only if they have the same
            character frequencies.

        Approach:
            Count character frequencies in both strings using Counter and
            compare the two counters for equality.

        Complexity:
            Time: O(n) where n is the length of the strings
            Space: O(1) since the alphabet size is fixed at 26
        """
        return Counter(s) == Counter(t)
