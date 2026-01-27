class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        """Prefix sum with hash map for maximum subarray length.

        Intuition:
            If prefix_sum[i] - prefix_sum[j] == k, then the subarray from j+1
            to i sums to k. Store the earliest index for each prefix sum.

        Approach:
            1. Maintain a running prefix sum and a dictionary mapping each sum
               to its earliest index.
            2. For each position, check if (prefix_sum - k) exists in the map
               and update the maximum length accordingly.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        prefix_index: dict[int, int] = {0: -1}
        result = prefix_sum = 0
        for idx, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - k in prefix_index:
                result = max(result, idx - prefix_index[prefix_sum - k])
            if prefix_sum not in prefix_index:
                prefix_index[prefix_sum] = idx
        return result
