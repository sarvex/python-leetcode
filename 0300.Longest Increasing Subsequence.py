class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """Dynamic programming approach tracking LIS ending at each index.

        Intuition:
            For each element, the longest increasing subsequence ending at that
            element depends on all previous elements that are smaller than it.

        Approach:
            1. Create a dp array where dp[i] represents the length of the LIS
               ending at index i, initialized to 1.
            2. For each index i, check all previous indices j. If nums[j] < nums[i],
               update dp[i] = max(dp[i], dp[j] + 1).
            3. Return the maximum value in the dp array.

        Complexity:
            Time: O(n^2) where n is the length of nums
            Space: O(n) for the dp array
        """
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
