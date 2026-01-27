from itertools import pairwise


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """Find all pairs with the minimum absolute difference.

        Intuition:
            After sorting, minimum differences only occur between adjacent
            elements. Find the minimum gap, then collect all pairs with that gap.

        Approach:
            Sort the array, compute the minimum adjacent difference, then filter
            all adjacent pairs matching that minimum difference.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        arr.sort()
        min_diff = min(b - a for a, b in pairwise(arr))
        return [[a, b] for a, b in pairwise(arr) if b - a == min_diff]
