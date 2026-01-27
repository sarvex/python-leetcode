class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        """Uncrossed Lines via Longest Common Subsequence DP.

        Intuition:
            This problem is equivalent to finding the longest common
            subsequence (LCS) between the two arrays, since uncrossed lines
            correspond to matching elements in order.

        Approach:
            Use a 2D DP table where dp[i][j] is the LCS length of
            nums1[:i] and nums2[:j]. If elements match, extend the diagonal.
            Otherwise, take the max of skipping either element.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        len1, len2 = len(nums1), len(nums2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len1][len2]
