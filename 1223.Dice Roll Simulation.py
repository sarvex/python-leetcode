from functools import cache


class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        """Dice roll simulation using memoized DFS.

        Intuition:
            At each roll, we can pick any face except continuing the current
            face beyond its rollMax limit. Track current face and consecutive count.

        Approach:
            Use top-down DP with memoization. State is (roll_index, last_face,
            consecutive_count). For each state, try all 6 faces, resetting or
            incrementing the consecutive counter accordingly.

        Complexity:
            Time: O(n * 6 * max(rollMax)) states with O(6) transitions each
            Space: O(n * 6 * max(rollMax)) for memoization
        """
        MOD = 10**9 + 7

        @cache
        def dfs(roll: int, last_face: int, consecutive: int) -> int:
            if roll >= n:
                return 1
            total = 0
            for face in range(1, 7):
                if face != last_face:
                    total += dfs(roll + 1, face, 1)
                elif consecutive < rollMax[last_face - 1]:
                    total += dfs(roll + 1, last_face, consecutive + 1)
            return total % MOD

        return dfs(0, 0, 0)
