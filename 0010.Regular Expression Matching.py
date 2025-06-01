from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Dynamic programming with memoization for regular expression matching.

        Intuition:
            Use recursion with memoization to check if a string matches a pattern.
            The key insight is handling the '*' pattern which can match zero or more
            of the preceding element.

        Approach:
            1. Use a recursive function with memoization to avoid redundant calculations
            2. Handle base case: if pattern is exhausted, string should also be exhausted
            3. Handle special case of '*': either skip the pattern or match current character
            4. For normal characters, match and move forward in both string and pattern

        Complexity:
            Time: O(m*n) where m is length of string and n is length of pattern
            Space: O(m*n) for the memoization cache
        """
        m, n = len(s), len(p)

        @cache
        def dfs(i: int, j: int) -> bool:
            # Base case: if pattern is exhausted
            if j >= n:
                return i == m

            # Check if next character is '*'
            has_star = j + 1 < n and p[j + 1] == '*'

            if has_star:
                # Either skip the '*' pattern (match 0 times)
                # Or match current character and stay on same pattern
                return dfs(i, j + 2) or (
                    i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j)
                )

            # Regular matching: current chars match and move forward in both strings
            return i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j + 1)

        return dfs(0, 0)
