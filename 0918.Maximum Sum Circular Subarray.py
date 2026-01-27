from math import inf


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """Prefix sum tracking for both max subarray and min subarray.

        Intuition:
            The maximum circular subarray sum is either a normal subarray
            (Kadane's) or a wrap-around subarray (total sum minus the minimum
            subarray). We can compute both in one pass using prefix sums.

        Approach:
            1. Track prefix sums while maintaining the minimum and maximum
               prefix sums seen so far.
            2. The max non-circular subarray is max(prefix_sum - min_prefix).
            3. The max circular subarray is total_sum - min(prefix_sum - max_prefix).
            4. Return the maximum of both.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        prefix_min, prefix_max = 0, -inf
        max_sum, running_sum, min_subarray = -inf, 0, inf
        for value in nums:
            running_sum += value
            max_sum = max(max_sum, running_sum - prefix_min)
            min_subarray = min(min_subarray, running_sum - prefix_max)
            prefix_min = min(prefix_min, running_sum)
            prefix_max = max(prefix_max, running_sum)
        return max(max_sum, running_sum - min_subarray)
