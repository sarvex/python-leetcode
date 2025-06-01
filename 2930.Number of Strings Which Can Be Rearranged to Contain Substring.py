from functools import cache

class Solution:
    def stringCount(self, n: int) -> int:
        """Count strings of length n that can be rearranged to contain 'leet'

        DP with state tracking for character counts

        Intuition: Track the minimum required characters ('l', 'e', 't') using DP states

        Approach: Use memoized recursion to track character counts needed.
        For each position, add either 'l', 'e', 't', or any other character.
        We need exactly 1 'l', 2 'e's, and 1 't' to form 'leet'.

        Complexity:
        Time: O(n) - At most n*3*3*2 states (position × l_count × e_count × t_count)
        Space: O(n) - For memoization cache
        """
        MOD = 10**9 + 7

        @cache
        def dfs(i: int, l_count: int, e_count: int, t_count: int) -> int:
            if i == 0:
                return int(l_count == 1 and e_count == 2 and t_count == 1)

            # Add character that's not 'l', 'e', or 't' (23 other letters)
            result = dfs(i - 1, l_count, e_count, t_count) * 23 % MOD

            # Try adding 'l', 'e', or 't' if needed
            if l_count < 1:
                result = (result + dfs(i - 1, l_count + 1, e_count, t_count)) % MOD
            if e_count < 2:
                result = (result + dfs(i - 1, l_count, e_count + 1, t_count)) % MOD
            if t_count < 1:
                result = (result + dfs(i - 1, l_count, e_count, t_count + 1)) % MOD

            return result

        return dfs(n, 0, 0, 0)
