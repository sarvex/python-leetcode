from functools import cache


class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        """Interval DP with memoization on box removal for maximum points.

        Intuition:
            When removing boxes, grouping same-colored boxes together yields
            more points (k+1)^2 vs multiple smaller removals. We need to
            consider merging non-adjacent same-colored boxes.

        Approach:
            Use top-down DP with state (left, right, streak) where streak
            counts consecutive same-colored boxes attached to boxes[right].
            Either remove the right group or find matching boxes to merge with.

        Complexity:
            Time: O(n^4)
            Space: O(n^3)
        """

        @cache
        def dfs(left: int, right: int, streak: int) -> int:
            if left > right:
                return 0
            while left < right and boxes[right] == boxes[right - 1]:
                right, streak = right - 1, streak + 1
            result = dfs(left, right - 1, 0) + (streak + 1) * (streak + 1)
            for mid in range(left, right):
                if boxes[mid] == boxes[right]:
                    result = max(
                        result, dfs(mid + 1, right - 1, 0) + dfs(left, mid, streak + 1)
                    )
            return result

        length = len(boxes)
        answer = dfs(0, length - 1, 0)
        dfs.cache_clear()
        return answer
