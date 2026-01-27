from math import inf

from sortedcontainers import SortedSet


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        """Find max rectangle sum no larger than k using sorted set with prefix sums.

        Intuition:
            Reduce the 2D problem to 1D by fixing row boundaries and computing
            column prefix sums. For each 1D array, find the max subarray sum
            no larger than k using a sorted set of prefix sums.

        Approach:
            Iterate over all pairs of row boundaries. For each pair, compress
            columns into a 1D array of cumulative sums. Then scan through the
            array maintaining a sorted set of prefix sums. For each current
            prefix sum s, find the smallest prefix sum p in the set such that
            s - p <= k (i.e., p >= s - k) using binary search.

        Complexity:
            Time: O(m^2 * n * log n) where m is rows and n is columns
            Space: O(n)
        """
        rows, cols = len(matrix), len(matrix[0])
        result = -inf
        for top in range(rows):
            column_sums = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    column_sums[col] += matrix[bottom][col]
                prefix_sum = 0
                sorted_prefixes = SortedSet([0])
                for value in column_sums:
                    prefix_sum += value
                    idx = sorted_prefixes.bisect_left(prefix_sum - k)
                    if idx != len(sorted_prefixes):
                        result = max(result, prefix_sum - sorted_prefixes[idx])
                    sorted_prefixes.add(prefix_sum)
        return result
