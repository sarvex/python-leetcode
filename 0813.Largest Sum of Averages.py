from functools import cache
from itertools import accumulate


class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        """Top-down DP with memoization to maximize sum of partition averages.

        Intuition:
            Try all possible first partition boundaries and recursively solve
            the remaining array with one fewer partition.

        Approach:
            1. Compute prefix sums for O(1) range sum queries.
            2. Use memoized DFS: at each state (start_index, partitions_left),
               try all split points and maximize the total average sum.
            3. Base case: one partition left returns the average of remaining elements.

        Complexity:
            Time: O(n^2 * k)
            Space: O(n * k)
        """

        @cache
        def dfs(start: int, partitions: int) -> float:
            if start == length:
                return 0
            if partitions == 1:
                return (prefix[length] - prefix[start]) / (length - start)
            best = 0.0
            for end in range(start, length):
                current_avg = (prefix[end + 1] - prefix[start]) / (end - start + 1)
                best = max(best, current_avg + dfs(end + 1, partitions - 1))
            return best

        length = len(nums)
        prefix = list(accumulate(nums, initial=0))
        return dfs(0, k)
