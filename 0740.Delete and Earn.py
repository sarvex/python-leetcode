from math import inf


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """House-robber DP on value frequencies.

        Intuition:
            Deleting a number earns its value but removes adjacent values, which
            is equivalent to the house-robber problem on the value axis.

        Approach:
            1. Sum contributions for each value into a total array.
            2. Apply the classic two-variable DP (skip or take) from 0 to max.

        Complexity:
            Time: O(N + M) where M = max(nums)
            Space: O(M)
        """
        max_val = -inf
        for num in nums:
            max_val = max(max_val, num)
        total = [0] * (max_val + 1)
        for num in nums:
            total[num] += num
        prev_skip = total[0]
        prev_take = max(total[0], total[1])
        for i in range(2, max_val + 1):
            current = max(prev_skip + total[i], prev_take)
            prev_skip = prev_take
            prev_take = current
        return prev_take
