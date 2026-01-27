from math import inf


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        """Find minimum positive start value so prefix sums stay positive.

        Intuition:
            The start value must offset the lowest prefix sum to keep the
            running total at least 1.

        Approach:
            Compute the minimum prefix sum. The answer is max(1, 1 - min_prefix)
            to ensure the running sum never drops below 1.

        Complexity:
            Time: O(n) single pass through nums
            Space: O(1) auxiliary space
        """
        prefix_sum = 0
        min_prefix = inf
        for num in nums:
            prefix_sum += num
            min_prefix = min(min_prefix, prefix_sum)
        return max(1, 1 - int(min_prefix))
