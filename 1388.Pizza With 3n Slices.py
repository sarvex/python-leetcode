class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        """Pick n non-adjacent slices from a circular arrangement to maximize sum.

        Intuition:
            Since slices are circular, choosing the first excludes the last.
            Reduce to two linear subproblems: exclude the last slice or
            exclude the first slice.

        Approach:
            For each linear subproblem, use DP where dp[i][j] is the maximum
            sum picking j slices from the first i. The recurrence either skips
            the current slice or takes it (requiring a gap of at least one).
            Return the maximum of both subproblems.

        Complexity:
            Time: O(n^2) where n is the number of slices divided by 3.
            Space: O(n^2)
        """

        def max_sum_non_adjacent(nums: list[int]) -> int:
            length = len(nums)
            dp = [[0] * (picks + 1) for _ in range(length + 1)]
            for i in range(1, length + 1):
                for j in range(1, picks + 1):
                    dp[i][j] = max(
                        dp[i - 1][j],
                        (dp[i - 2][j - 1] if i >= 2 else 0) + nums[i - 1],
                    )
            return dp[length][picks]

        picks = len(slices) // 3
        exclude_last = max_sum_non_adjacent(slices[:-1])
        exclude_first = max_sum_non_adjacent(slices[1:])
        return max(exclude_last, exclude_first)
