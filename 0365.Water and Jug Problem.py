class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        """Determine if target volume is measurable using DFS state exploration.

        Intuition:
            Model the problem as a graph where each state is (jug1, jug2)
            volumes. From any state, we can fill, empty, or pour between jugs.
            Search for a state that sums to the target.

        Approach:
            Use recursive DFS with memoization via a visited set. From each
            state (jug1, jug2), try all six operations: fill either jug, empty
            either jug, or pour from one to another. Return True if any state
            has jug1 == z, jug2 == z, or jug1 + jug2 == z.

        Complexity:
            Time: O(x * y) for all possible states
            Space: O(x * y) for the visited set
        """

        def dfs(jug1: int, jug2: int) -> bool:
            if (jug1, jug2) in visited:
                return False
            visited.add((jug1, jug2))
            if jug1 == z or jug2 == z or jug1 + jug2 == z:
                return True
            if dfs(x, jug2) or dfs(jug1, y) or dfs(0, jug2) or dfs(jug1, 0):
                return True
            pour_to_jug2 = min(jug1, y - jug2)
            pour_to_jug1 = min(jug2, x - jug1)
            return dfs(jug1 - pour_to_jug2, jug2 + pour_to_jug2) or dfs(
                jug1 + pour_to_jug1, jug2 - pour_to_jug1
            )

        visited: set[tuple[int, int]] = set()
        return dfs(0, 0)
