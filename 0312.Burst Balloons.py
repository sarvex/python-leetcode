class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """Interval DP treating each balloon as the last burst in its range.

        Intuition:
            Instead of choosing which balloon to burst first, think of which
            balloon is burst last in each subrange. This gives independent
            subproblems on the left and right.

        Approach:
            1. Pad nums with 1 on both ends to handle boundary cases.
            2. Define dp[i][j] as the max coins from bursting all balloons
               between indices i and j (exclusive).
            3. For each interval, try each balloon k as the last to burst,
               earning arr[i]*arr[k]*arr[j] plus the subproblems.

        Complexity:
            Time: O(n^3) where n is the length of nums
            Space: O(n^2) for the dp table
        """
        length = len(nums)
        arr = [1] + nums + [1]
        dp = [[0] * (length + 2) for _ in range(length + 2)]
        for i in range(length - 1, -1, -1):
            for j in range(i + 2, length + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                    )
        return dp[0][-1]
