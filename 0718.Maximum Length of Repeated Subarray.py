class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        """Dynamic programming to find longest common subarray.

        Intuition:
            This is equivalent to finding the longest common substring between
            two sequences, which can be solved with a 2D DP table.

        Approach:
            1. Build dp[i][j] = length of longest common subarray ending at
               nums1[i-1] and nums2[j-1].
            2. If nums1[i-1] == nums2[j-1], extend the previous diagonal.
            3. Track the maximum value seen across the entire table.

        Complexity:
            Time: O(m * n) where m, n are lengths of nums1, nums2
            Space: O(m * n) for the DP table
        """
        length1, length2 = len(nums1), len(nums2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        result = 0
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        return result
