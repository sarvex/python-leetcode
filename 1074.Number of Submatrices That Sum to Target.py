from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        """Count submatrices that sum to target.

        Intuition:
            Reduce 2D problem to 1D by fixing row boundaries and using prefix
            sum technique on compressed columns.

        Approach:
            For each pair of top/bottom rows, compress columns into a 1D array.
            Apply the subarray-sum-equals-k technique with a hash map.

        Complexity:
            Time: O(m^2 * n) where m = rows, n = columns
            Space: O(n) for column sums and prefix map
        """

        def count_subarrays_with_target(nums: list[int]) -> int:
            prefix_counts: dict[int, int] = defaultdict(int)
            prefix_counts[0] = 1
            count = prefix_sum = 0
            for value in nums:
                prefix_sum += value
                count += prefix_counts[prefix_sum - target]
                prefix_counts[prefix_sum] += 1
            return count

        row_count, col_count = len(matrix), len(matrix[0])
        total = 0
        for top in range(row_count):
            col_sums = [0] * col_count
            for bottom in range(top, row_count):
                for col in range(col_count):
                    col_sums[col] += matrix[bottom][col]
                total += count_subarrays_with_target(col_sums)
        return total
