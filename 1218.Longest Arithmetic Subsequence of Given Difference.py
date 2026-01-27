from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        """Longest arithmetic subsequence of given difference.

        Intuition:
            For each element, the longest subsequence ending at it extends the
            subsequence ending at (element - difference) by one.

        Approach:
            Use a hash map to store the longest subsequence length ending at each
            value. For each element x, set dp[x] = dp[x - difference] + 1.

        Complexity:
            Time: O(n) where n is the length of the array
            Space: O(n) for the hash map
        """
        dp: defaultdict[int, int] = defaultdict(int)
        for value in arr:
            dp[value] = dp[value - difference] + 1
        return max(dp.values())
