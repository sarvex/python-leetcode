class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        """Two-pointer greedy on sorted jobs and workers.

        Intuition:
            Sort jobs by difficulty and workers by ability. For each worker,
            find the best profit among all jobs they can handle.

        Approach:
            1. Sort workers and jobs (by difficulty).
            2. Use a pointer to track the best available profit as workers
               increase in ability.
            3. Accumulate the best profit for each worker.

        Complexity:
            Time: O(n log n + m log m) where n = jobs, m = workers
            Space: O(n)
        """
        worker.sort()
        jobs = sorted(zip(difficulty, profit))
        total_profit = max_profit = job_idx = 0
        for ability in worker:
            while job_idx < len(jobs) and jobs[job_idx][0] <= ability:
                max_profit = max(max_profit, jobs[job_idx][1])
                job_idx += 1
            total_profit += max_profit
        return total_profit
