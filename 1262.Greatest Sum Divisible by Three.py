import math


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        """Find the maximum sum of elements divisible by three.

        Intuition:
            Track the best achievable sum for each remainder (0, 1, 2) when
            divided by 3. Each new number transitions between remainder states.

        Approach:
            Use DP where dp[i][j] is the maximum sum using the first i numbers
            with remainder j mod 3. For each number, either skip it or add it,
            transitioning from remainder (j - x) % 3 to remainder j.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        count = len(nums)
        dp = [[-math.inf] * 3 for _ in range(count + 1)]
        dp[0][0] = 0
        for i, x in enumerate(nums, 1):
            for j in range(3):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][(j - x) % 3] + x)
        return dp[count][0]
