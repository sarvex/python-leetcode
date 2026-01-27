from functools import cache


class Solution:
    def checkRecord(self, n: int) -> int:
        """Count eligible attendance records of length n using memoized DFS.

        Intuition:
            Each position can be P, A, or L with constraints on total absences
            and consecutive lates. We can model this as a state machine with
            memoization on (position, absence_count, consecutive_late_count).

        Approach:
            1. Use DFS with memoization tracking day index, absences used, and
               consecutive lates.
            2. At each step, try adding P (resets late), A (if none used), or
               L (if fewer than 2 consecutive).
            3. Return results modulo 10^9 + 7.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        @cache
        def dfs(day: int, absences: int, consecutive_lates: int) -> int:
            if day >= n:
                return 1
            result = 0
            if absences == 0:
                result += dfs(day + 1, absences + 1, 0)
            if consecutive_lates < 2:
                result += dfs(day + 1, absences, consecutive_lates + 1)
            result += dfs(day + 1, absences, 0)
            return result % modulo

        modulo = 10**9 + 7
        answer = dfs(0, 0, 0)
        dfs.cache_clear()
        return answer
