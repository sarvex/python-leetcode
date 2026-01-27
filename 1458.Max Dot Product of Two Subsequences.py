from math import inf


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        """Find maximum dot product of non-empty subsequences from two arrays.

        Intuition:
            Similar to longest common subsequence but maximizing the dot product
            sum, choosing at least one pair.

        Approach:
            Use 2D DP where dp[i][j] is the maximum dot product using
            subsequences from nums1[:i] and nums2[:j]. For each pair, either
            skip one element or include the product of nums1[i-1]*nums2[j-1]
            added to the best previous state (or starting fresh if previous was
            negative).

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        m, n = len(nums1), len(nums2)
        dp = [[-inf] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    dp[i - 1][j], dp[i][j - 1], max(dp[i - 1][j - 1], 0) + product
                )
        return dp[-1][-1]
