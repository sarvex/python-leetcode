class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """Single Pass Character Comparison.

        Intuition:
            Two strings are one edit distance apart if they differ by exactly
            one insertion, deletion, or replacement. Ensure the longer string
            is always first to simplify logic.

        Approach:
            Ensure s is the longer string. If the length difference exceeds 1,
            return False. Scan characters; at the first mismatch, check if the
            remaining substrings match (either skipping one char in s for
            deletion, or skipping one in both for replacement).

        Complexity:
            Time: O(n) single pass through the shorter string
            Space: O(n) for substring slicing comparisons
        """
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        len_s, len_t = len(s), len(t)
        if len_s - len_t > 1:
            return False
        for i, char in enumerate(t):
            if char != s[i]:
                return (
                    s[i + 1 :] == t[i + 1 :] if len_s == len_t else s[i + 1 :] == t[i:]
                )
        return len_s == len_t + 1
