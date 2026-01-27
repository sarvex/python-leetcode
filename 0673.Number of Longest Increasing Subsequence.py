class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        """DP tracking both LIS length and count for each position.

        Intuition:
        Extend the standard LIS DP to also count the number of subsequences
        achieving the maximum length at each position.

        Approach:
        1. For each element, compare with all previous elements.
        2. If a longer subsequence is found ending here, update length and inherit count.
        3. If same-length subsequence found, add to the count.
        4. Track the global maximum length and sum up counts of all positions with that length.

        Complexity:
        Time: O(n^2)
        Space: O(n)
        """
        length = len(nums)
        dp_len = [1] * length
        dp_count = [1] * length
        max_len = 0
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp_len[i] < dp_len[j] + 1:
                        dp_len[i] = dp_len[j] + 1
                        dp_count[i] = dp_count[j]
                    elif dp_len[i] == dp_len[j] + 1:
                        dp_count[i] += dp_count[j]
            if max_len < dp_len[i]:
                max_len = dp_len[i]
                result = dp_count[i]
            elif max_len == dp_len[i]:
                result += dp_count[i]
        return result
