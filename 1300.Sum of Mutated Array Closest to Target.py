from bisect import bisect_right
from itertools import accumulate
from math import inf


class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        """Find the value to mutate array elements so the sum is closest to target.

        Intuition:
            For a given threshold value, all elements greater than it become that value.
            The resulting sum is monotonically non-decreasing, so we can enumerate all
            possible values.

        Approach:
            Sort the array and compute prefix sums. For each candidate value from 0 to
            max(arr), use binary search to find how many elements exceed it, compute the
            resulting sum, and track the value with minimum absolute difference to target.

        Complexity:
            Time: O(n log n + M log n) where M = max(arr)
            Space: O(n)
        """
        arr.sort()
        prefix = list(accumulate(arr, initial=0))
        best_value, min_diff = 0, inf
        for value in range(max(arr) + 1):
            index = bisect_right(arr, value)
            current_sum = prefix[index] + (len(arr) - index) * value
            diff = abs(current_sum - target)
            if min_diff > diff:
                min_diff = diff
                best_value = value
        return best_value
