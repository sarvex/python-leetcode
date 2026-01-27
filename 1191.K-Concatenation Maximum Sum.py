class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        """Maximum subarray sum of k concatenated copies of arr.

        Intuition:
            For k=1, it's Kadane's algorithm. For k>=2, the answer may include
            the maximum suffix of one copy plus the maximum prefix of another,
            plus (k-2) full copies if the total sum is positive.

        Approach:
            Compute max subarray sum, max prefix sum, and max suffix sum in one
            pass. For k>=2, consider combining suffix + prefix, and if array
            sum is positive, add (k-2) full array sums.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        MOD = 10**9 + 7
        total_sum = max_prefix = min_prefix = max_subarray = 0
        for value in arr:
            total_sum += value
            max_prefix = max(max_prefix, total_sum)
            min_prefix = min(min_prefix, total_sum)
            max_subarray = max(max_subarray, total_sum - min_prefix)
        result = max_subarray
        if k == 1:
            return result % MOD
        max_suffix = total_sum - min_prefix
        result = max(result, max_prefix + max_suffix)
        if total_sum > 0:
            result = max(result, (k - 2) * total_sum + max_prefix + max_suffix)
        return result % MOD
