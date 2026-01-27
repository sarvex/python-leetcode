from bisect import bisect_left
from itertools import accumulate


class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree) for prefix sum queries.

    Supports point updates and prefix sum queries in O(log n) time.
    """

    def __init__(self, size: int) -> None:
        """Initialize tree with given size."""
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Add delta to element at index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        """Return prefix sum from 1 to index."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        """BIT with coordinate compression to count range sums.

        Intuition:
            Using prefix sums, a range sum [i, j] equals prefix[j+1] - prefix[i].
            We need to count pairs where lower <= prefix[j] - prefix[i] <= upper.

        Approach:
            1. Compute prefix sums and collect all relevant values for
               coordinate compression.
            2. Use a Binary Indexed Tree to efficiently count how many previous
               prefix sums fall within the valid range for each new prefix sum.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        prefix_sums = list(accumulate(nums, initial=0))
        sorted_vals = sorted(
            set(
                val
                for prefix in prefix_sums
                for val in (prefix, prefix - lower, prefix - upper)
            )
        )
        tree = BinaryIndexedTree(len(sorted_vals))
        result = 0
        for prefix in prefix_sums:
            left = bisect_left(sorted_vals, prefix - upper) + 1
            right = bisect_left(sorted_vals, prefix - lower) + 1
            result += tree.query(right) - tree.query(left - 1)
            tree.update(bisect_left(sorted_vals, prefix) + 1, 1)
        return result
