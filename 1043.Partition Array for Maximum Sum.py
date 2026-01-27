class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        """Partition Array for Maximum Sum using dynamic programming.

        Intuition:
            For each position, try all valid partition lengths up to k and
            pick the one that maximizes the sum using the partition's max value.

        Approach:
            Use DP where dp[i] is the maximum sum for arr[:i]. For each i,
            look back up to k elements, track the running maximum in the
            partition, and compute dp[i] = max(dp[j-1] + max_val * (i-j+1)).

        Complexity:
            Time: O(n * k)
            Space: O(n)
        """
        length = len(arr)
        dp = [0] * (length + 1)
        for i in range(1, length + 1):
            partition_max = 0
            for j in range(i, max(0, i - k), -1):
                partition_max = max(partition_max, arr[j - 1])
                dp[i] = max(dp[i], dp[j - 1] + partition_max * (i - j + 1))
        return dp[length]
