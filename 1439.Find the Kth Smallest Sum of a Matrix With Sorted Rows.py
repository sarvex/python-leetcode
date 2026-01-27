class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        """Find kth smallest sum picking one element from each sorted row.

        Intuition:
            Merge rows one at a time, keeping only the k smallest partial sums
            since we only need the kth smallest overall.

        Approach:
            Start with a list containing 0. For each row, generate all possible
            sums by adding each row element to existing partial sums, sort them,
            and keep only the top k candidates.

        Complexity:
            Time: O(m * k * n * log(k * n)) where m is rows and n is columns
            Space: O(k) for storing partial sums
        """
        partial_sums = [0]
        for row in mat:
            partial_sums = sorted(
                total + value for total in partial_sums for value in row[:k]
            )[:k]
        return partial_sums[-1]
