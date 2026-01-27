from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Memoized DFS with Two Pointers

        Intuition:
            At each step we can take a character from either s1 or s2 as long
            as it matches the current character in s3. This forms a decision
            tree that can be pruned with memoization.

        Approach:
            Use a recursive DFS with two indices tracking positions in s1 and
            s2. The position in s3 is implicitly i + j. At each step, try
            matching the current s3 character with s1[i] or s2[j] and recurse.
            Cache results to avoid recomputation.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """

        @cache
        def dfs(i: int, j: int) -> bool:
            if i >= len_s1 and j >= len_s2:
                return True
            k = i + j
            if i < len_s1 and s1[i] == s3[k] and dfs(i + 1, j):
                return True
            if j < len_s2 and s2[j] == s3[k] and dfs(i, j + 1):
                return True
            return False

        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 + len_s2 != len(s3):
            return False
        return dfs(0, 0)
