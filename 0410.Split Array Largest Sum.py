from bisect import bisect_left
from math import inf


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        """Binary search on the answer with greedy feasibility check.

        Intuition:
            The minimum largest sum is bounded between max(nums) and sum(nums).
            We can binary search this range and greedily check if a given
            maximum subarray sum allows splitting into at most k parts.

        Approach:
            1. Set search range: left = max(nums), right = sum(nums).
            2. Binary search for the smallest maximum sum that is feasible.
            3. Feasibility check: greedily accumulate elements; when the
               running sum exceeds the candidate max, start a new partition.
            4. The candidate is feasible if partitions needed <= k.

        Complexity:
            Time: O(n * log(sum - max))
            Space: O(1)
        """

        def check(max_sum: int) -> bool:
            running_sum: int | float = inf
            partition_count = 0
            for value in nums:
                running_sum += value
                if running_sum > max_sum:
                    running_sum = value
                    partition_count += 1
            return partition_count <= k

        left, right = max(nums), sum(nums)
        return left + bisect_left(range(left, right + 1), True, key=check)
