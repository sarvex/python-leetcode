from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """Memoized Recursive Approach

        Intuition:
            A scrambled string can be formed by splitting at any index and
            optionally swapping the two parts, then recursively scrambling
            each part.

        Approach:
            Use a recursive function with memoization parameterized by
            start indices in s1 and s2 and the substring length. For each
            possible split point, check two cases: no swap (both halves
            correspond directly) and swap (first half of s1 matches second
            half of s2 and vice versa).

        Complexity:
            Time: O(n^4) where n is the length of the strings
            Space: O(n^3) for memoization
        """

        @cache
        def dfs(start1: int, start2: int, length: int) -> bool:
            if length == 1:
                return s1[start1] == s2[start2]
            for split in range(1, length):
                if dfs(start1, start2, split) and dfs(
                    start1 + split, start2 + split, length - split
                ):
                    return True
                if dfs(start1 + split, start2, length - split) and dfs(
                    start1, start2 + length - split, split
                ):
                    return True
            return False

        return dfs(0, 0, len(s1))
