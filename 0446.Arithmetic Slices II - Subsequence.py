from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """Dynamic programming with hash maps tracking arithmetic subsequences by difference.

        Intuition:
            For each pair (j, i), the common difference d = nums[i] - nums[j].
            The number of arithmetic subsequences of length >= 3 ending at i
            with difference d includes all subsequences ending at j with the same d.

        Approach:
            1. For each index i, maintain a dictionary mapping common difference
               to the count of arithmetic subsequences ending at i.
            2. For each pair (j, i) where j < i, compute d = nums[i] - nums[j].
            3. Add dp[j][d] to the answer (these are subsequences of length >= 3).
            4. Update dp[i][d] += dp[j][d] + 1 (the +1 accounts for the pair itself).

        Complexity:
            Time: O(n^2) for all pairs.
            Space: O(n^2) for the DP hash maps.
        """
        dp = [defaultdict(int) for _ in nums]
        total = 0
        for i, current in enumerate(nums):
            for j, previous in enumerate(nums[:i]):
                difference = current - previous
                total += dp[j][difference]
                dp[i][difference] += dp[j][difference] + 1
        return total
