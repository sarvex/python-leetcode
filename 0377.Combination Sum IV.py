class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """Count combinations that sum to target using bottom-up DP.

        Intuition:
            This is a permutation problem where order matters. For each target
            value, any number from nums can be the last element added.

        Approach:
            Use a 1D DP array where dp[i] represents the number of ways to
            reach sum i. For each sum from 1 to target, iterate over all
            numbers in nums and add dp[i - x] if i >= x. Base case: dp[0] = 1.

        Complexity:
            Time: O(target * n) where n is the length of nums
            Space: O(target)
        """
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]
