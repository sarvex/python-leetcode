class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """Dynamic programming with subset sum transformation.

        Intuition:
            The problem can be transformed into a subset sum problem. If we split
            nums into positive set P and negative set N, then sum(P) - sum(N) = target
            and sum(P) + sum(N) = total, so sum(N) = (total - target) / 2.

        Approach:
            Transform to counting subsets that sum to (total - target) / 2 using
            a 2D DP table where dp[i][j] = number of ways to make sum j using
            first i elements.

        Complexity:
            Time: O(m * n) where m is length of nums and n is (total - target) / 2
            Space: O(m * n)
        """
        total = sum(nums)
        if total < target or (total - target) % 2:
            return 0
        num_items, neg_sum = len(nums), (total - target) // 2
        dp = [[0] * (neg_sum + 1) for _ in range(num_items + 1)]
        dp[0][0] = 1
        for i, value in enumerate(nums, 1):
            for j in range(neg_sum + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= value:
                    dp[i][j] += dp[i - 1][j - value]
        return dp[num_items][neg_sum]
