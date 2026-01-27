class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """2D dynamic programming for subset sum targeting half the total.

        Intuition:
            Partitioning into two equal subsets is equivalent to finding a subset
            that sums to exactly half the total sum.

        Approach:
            1. If total sum is odd, return False immediately.
            2. Build a 2D DP table where dp[i][j] indicates whether the first i
               numbers can form a subset summing to j.
            3. For each number, either skip it or include it if j >= nums[i].
            4. Return dp[n][half].

        Complexity:
            Time: O(n * half) where half is sum(nums) // 2.
            Space: O(n * half) for the DP table.
        """
        half, remainder = divmod(sum(nums), 2)
        if remainder:
            return False
        count = len(nums)
        dp = [[False] * (half + 1) for _ in range(count + 1)]
        dp[0][0] = True
        for i, value in enumerate(nums, 1):
            for target in range(half + 1):
                dp[i][target] = dp[i - 1][target] or (
                    target >= value and dp[i - 1][target - value]
                )
        return dp[count][half]
