class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Two-pointer approach to check if s is a subsequence of t.

        Intuition:
            Use two pointers to track positions in both strings. When characters match,
            advance both pointers; otherwise, only advance in the target string.

        Approach:
            1. Initialize two pointers, one for each string
            2. Iterate through both strings, advancing pointers based on character matches
            3. If we can match all characters in s, it's a subsequence

        Complexity:
            Time: O(n), where n is the length of string t
            Space: O(1), only using two pointer variables
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
