from collections import Counter
from math import factorial, isqrt


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        """Count permutations where every adjacent pair sums to a perfect square.

        Intuition:
            Use bitmask DP to enumerate permutations, checking the squareful
            condition for adjacent elements. Divide by duplicate counts at the end.

        Approach:
            Let f[mask][j] = number of permutations of the subset represented by
            mask that end with element j. Transition by adding element k if the
            sum nums[j] + nums[k] is a perfect square. Final answer accounts for
            duplicate elements via factorial division.

        Complexity:
            Time: O(2^n * n^2) where n is the length of nums
            Space: O(2^n * n) for the DP table
        """
        length = len(nums)
        dp = [[0] * length for _ in range(1 << length)]
        for j in range(length):
            dp[1 << j][j] = 1
        for mask in range(1 << length):
            for j in range(length):
                if mask >> j & 1:
                    for k in range(length):
                        if (mask >> k & 1) and k != j:
                            pair_sum = nums[j] + nums[k]
                            root = isqrt(pair_sum)
                            if root * root == pair_sum:
                                dp[mask][j] += dp[mask ^ (1 << j)][k]

        total = sum(dp[(1 << length) - 1][j] for j in range(length))
        for count in Counter(nums).values():
            total //= factorial(count)
        return total
