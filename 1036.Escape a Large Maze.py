class Solution:
    def isEscapePossible(
        self, blocked: list[list[int]], source: list[int], target: list[int]
    ) -> bool:
        """Escape a Large Maze using limited BFS/DFS with area bound.

        Intuition:
            With at most 200 blocked cells, the maximum enclosed area is
            bounded by ~20000 cells. If DFS from a point visits more cells
            than this bound without being trapped, the point is not enclosed.

        Approach:
            Run DFS from source toward target and from target toward source.
            If either search gets trapped (visits fewer than the threshold
            cells without reaching the other point), return False. Both
            searches must escape or meet for the answer to be True.

        Complexity:
            Time: O(B^2) where B is the number of blocked cells
            Space: O(B^2)
        """

        def search(
            start: list[int], goal: list[int], seen: set[tuple[int, int]]
        ) -> bool:
            row, col = start
            if (
                not (0 <= row < 10**6 and 0 <= col < 10**6)
                or (row, col) in blocked_set
                or (row, col) in seen
            ):
                return False
            seen.add((row, col))
            if len(seen) > 20000 or start == goal:
                return True
            for delta_r, delta_c in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                if search([row + delta_r, col + delta_c], goal, seen):
                    return True
            return False

        blocked_set = {(row, col) for row, col in blocked}
        return search(source, target, set()) and search(target, source, set())
