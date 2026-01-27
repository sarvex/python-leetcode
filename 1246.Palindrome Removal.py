from math import inf


class Solution:
    def minimumMoves(self, arr: list[int]) -> int:
        """Remove palindromic subarrays with minimum moves using interval DP.

        Intuition:
            A palindromic subarray can be removed in one move. We want to minimize
            the total number of moves. If two endpoints match, they can potentially
            be removed together with the inner palindrome, reducing the cost.

        Approach:
            Use interval DP where dp[i][j] represents the minimum moves to remove
            arr[i..j]. For each interval, if arr[i] == arr[j], we can potentially
            merge their removal with the inner subarray. We also try all possible
            split points to find the optimal partition.

        Complexity:
            Time: O(n^3) — three nested loops over the array length
            Space: O(n^2) — for the DP table
        """
        length = len(arr)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if i + 1 == j:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    best = dp[i + 1][j - 1] if arr[i] == arr[j] else inf
                    for k in range(i, j):
                        best = min(best, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = best
        return dp[0][length - 1]
