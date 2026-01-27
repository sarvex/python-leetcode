class Solution:
    def longestPrefix(self, s: str) -> str:
        """Find the longest prefix that is also a suffix.

        Intuition:
            A happy prefix is a non-empty prefix that is also a suffix
            (excluding the entire string). Check from shortest skip.

        Approach:
            Iterate through possible split points. For each split at index i,
            check if the prefix s[:-i] equals the suffix s[i:]. Return the
            first match found.

        Complexity:
            Time: O(n^2) for string comparison at each split point
            Space: O(n) for string slicing
        """
        for i in range(1, len(s)):
            if s[:-i] == s[i:]:
                return s[i:]
        return ""
