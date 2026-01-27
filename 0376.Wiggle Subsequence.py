class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        """Find longest wiggle subsequence using two-state DP.

        Intuition:
            A wiggle subsequence alternates between increasing and decreasing.
            Track two states: subsequences ending with an up-wiggle and those
            ending with a down-wiggle.

        Approach:
            Use two DP arrays: up[i] for the longest wiggle subsequence ending
            at i with an upward wiggle, and down[i] for a downward wiggle.
            For each pair (i, j), if nums[j] < nums[i], update up[i] from
            down[j] + 1. If nums[j] > nums[i], update down[i] from up[j] + 1.
            Track the overall maximum.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        length = len(nums)
        max_length = 1
        up = [1] * length
        down = [1] * length
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)
            max_length = max(max_length, up[i], down[i])
        return max_length
