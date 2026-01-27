from math import inf


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        """Find minimum total Manhattan distance to assign bikes to workers.

        Intuition:
            Use bitmask DP to try all bike assignments and find the minimum cost.

        Approach:
            dp[i][mask] = min cost to assign bikes to the first i workers where
            mask represents which bikes are used. Enumerate all bike selections
            for each worker.

        Complexity:
            Time: O(n * 2^m * m) where n = workers, m = bikes
            Space: O(n * 2^m)
        """
        worker_count, bike_count = len(workers), len(bikes)
        dp = [[inf] * (1 << bike_count) for _ in range(worker_count + 1)]
        dp[0][0] = 0
        for i, (wx, wy) in enumerate(workers, 1):
            for mask in range(1 << bike_count):
                for k, (bx, by) in enumerate(bikes):
                    if mask >> k & 1:
                        dp[i][mask] = min(
                            dp[i][mask],
                            dp[i - 1][mask ^ (1 << k)] + abs(wx - bx) + abs(wy - by),
                        )
        return min(dp[worker_count])
