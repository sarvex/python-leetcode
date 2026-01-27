from itertools import accumulate


class Solution:
    def dietPlanPerformance(
        self, calories: list[int], k: int, lower: int, upper: int
    ) -> int:
        """Evaluate diet plan performance using sliding window sums.

        Intuition:
            For each consecutive k-day window, compare the calorie sum against
            lower and upper thresholds to accumulate points.

        Approach:
            Build a prefix sum array, then iterate over all windows of size k,
            subtracting a point when below lower and adding one when above upper.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        prefix = list(accumulate(calories, initial=0))
        points = 0
        total_days = len(calories)
        for i in range(total_days - k + 1):
            window_sum = prefix[i + k] - prefix[i]
            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1
        return points
