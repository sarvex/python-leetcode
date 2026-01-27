from functools import cache


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        """Count non-crossing handshake arrangements for people in a circle.

        Intuition:
            This is a Catalan number variant. Fixing one person's handshake
            partner divides the remaining people into two independent groups
            that must each have an even count.

        Approach:
            Use memoized recursion. For i people, try all valid partners for
            the first person (only even-gap positions), splitting the circle
            into two independent subproblems of sizes l and i-l-2.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """

        @cache
        def dfs(people: int) -> int:
            if people < 2:
                return 1
            total = 0
            for left in range(0, people, 2):
                right = people - left - 2
                total += dfs(left) * dfs(right)
                total %= MOD
            return total

        MOD = 10**9 + 7
        return dfs(numPeople)
