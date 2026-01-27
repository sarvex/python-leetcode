from functools import cache


class Solution:
    def minInsertions(self, s: str) -> int:
        """Minimum insertions to make a string palindrome.

        Intuition:
            If outer characters match, recurse inward. Otherwise, try inserting
            a character on either end and take the minimum.

        Approach:
            Use top-down DP with memoization. For substring s[i..j], if s[i] == s[j],
            the answer is the same as s[i+1..j-1]. Otherwise, it is 1 + min of
            solving s[i+1..j] or s[i..j-1].

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """

        @cache
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
            if s[left] == s[right]:
                return dp(left + 1, right - 1)
            return 1 + min(dp(left + 1, right), dp(left, right - 1))

        return dp(0, len(s) - 1)
