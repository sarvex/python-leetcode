class Solution:
    def numRollsToTarget(self, num_dice: int, num_faces: int, target: int) -> int:
        """Count ways to roll dice to reach target sum using dynamic programming.

        Intuition:
            Each die adds 1..k to the running total. We can build up the count
            of ways to reach each sum using the results from fewer dice.

        Approach:
            Use a 2D DP table where dp[i][j] is the number of ways to get sum j
            using i dice. For each die, iterate over possible sums and face values.

        Complexity:
            Time: O(n * target * k)
            Space: O(n * target)
        """
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
        dp[0][0] = 1
        for i in range(1, num_dice + 1):
            for j in range(1, min(i * num_faces, target) + 1):
                for face in range(1, min(j, num_faces) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD
        return dp[num_dice][target]
