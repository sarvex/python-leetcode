from math import inf


class Solution:
    def minDifficulty(self, job_difficulty: list[int], d: int) -> int:
        """Schedule jobs over d days minimizing total difficulty.

        Intuition:
            Each day must have at least one job. The difficulty of a day is the
            max job difficulty that day. Use DP to partition jobs into d groups.

        Approach:
            dp[i][j] = min difficulty to schedule first i jobs in j days.
            For each day j, try all possible last-day partitions and track the
            running maximum difficulty.

        Complexity:
            Time: O(n^2 * d)
            Space: O(n * d)
        """
        num_jobs = len(job_difficulty)
        dp = [[inf] * (d + 1) for _ in range(num_jobs + 1)]
        dp[0][0] = 0
        for i in range(1, num_jobs + 1):
            for j in range(1, min(d + 1, i + 1)):
                max_difficulty = 0
                for k in range(i, 0, -1):
                    max_difficulty = max(max_difficulty, job_difficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + max_difficulty)
        return -1 if dp[num_jobs][d] >= inf else dp[num_jobs][d]
