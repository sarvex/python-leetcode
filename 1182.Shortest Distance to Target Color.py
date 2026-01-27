from math import inf


class Solution:
    def shortestDistanceColor(
        self, colors: list[int], queries: list[list[int]]
    ) -> list[int]:
        """Find shortest distance to target color for each query.

        Intuition:
            Precompute nearest occurrence of each color from both left and right
            directions so each query can be answered in O(1).

        Approach:
            Build two arrays: right_nearest[i][c] stores the nearest index of color
            c at or after position i, and left_nearest[i][c] stores the nearest index
            at or before position i. Answer each query by taking the minimum distance
            from both directions.

        Complexity:
            Time: O(n + q)
            Space: O(n)
        """
        n = len(colors)
        right_nearest: list[list[float]] = [[inf] * 3 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(3):
                right_nearest[i][j] = right_nearest[i + 1][j]
            right_nearest[i][colors[i] - 1] = i

        left_nearest: list[list[float]] = [[-inf] * 3 for _ in range(n + 1)]
        for i, color in enumerate(colors, 1):
            for j in range(3):
                left_nearest[i][j] = left_nearest[i - 1][j]
            left_nearest[i][color - 1] = i - 1

        result: list[int] = []
        for index, target_color in queries:
            distance = min(
                index - left_nearest[index + 1][target_color - 1],
                right_nearest[index][target_color - 1] - index,
            )
            result.append(-1 if distance > n else int(distance))
        return result
