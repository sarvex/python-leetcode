from bisect import bisect_left
from functools import cache


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        """Find the maximum profit from non-overlapping job scheduling.

        Intuition:
            Sort jobs by start time. For each job, decide to either skip it
            or take it and jump to the next non-overlapping job using binary
            search.

        Approach:
            Sort jobs by start time. Use top-down DP with memoization. For
            each job index, binary search for the earliest job starting at or
            after the current job's end time, then take the maximum of skipping
            versus taking the current job.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """

        @cache
        def dfs(i: int) -> int:
            if i >= job_count:
                return 0
            _, end, pay = jobs[i]
            next_job = bisect_left(jobs, end, lo=i + 1, key=lambda x: x[0])
            return max(dfs(i + 1), pay + dfs(next_job))

        jobs = sorted(zip(startTime, endTime, profit))
        job_count = len(profit)
        return dfs(0)
