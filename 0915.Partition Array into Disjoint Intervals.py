from math import inf


class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        """Suffix minimum array with prefix maximum scan.

        Intuition:
            Find the earliest split where the maximum of the left part is
            less than or equal to the minimum of the right part.

        Approach:
            1. Precompute suffix minimums from right to left.
            2. Scan left to right tracking the running maximum.
            3. Return the first position where the prefix max <= suffix min.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(nums)
        suffix_min: list[float] = [inf] * (length + 1)
        for idx in range(length - 1, -1, -1):
            suffix_min[idx] = min(nums[idx], suffix_min[idx + 1])
        prefix_max = 0
        for idx, value in enumerate(nums, 1):
            prefix_max = max(prefix_max, value)
            if prefix_max <= suffix_min[idx]:
                return idx
        return length
