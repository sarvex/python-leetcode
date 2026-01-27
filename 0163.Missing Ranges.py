from itertools import pairwise


class Solution:
    def findMissingRanges(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        """Linear Scan with Gap Detection.

        Intuition:
            Scan through the sorted array and identify gaps between consecutive
            elements, as well as gaps at the boundaries.

        Approach:
            Check for a gap before the first element and after the last element.
            For each consecutive pair, check if there is a gap larger than 1
            and record the missing range.

        Complexity:
            Time: O(n) single pass through the array
            Space: O(1) excluding the output list
        """
        num_count = len(nums)
        if num_count == 0:
            return [[lower, upper]]
        result: list[list[int]] = []
        if nums[0] > lower:
            result.append([lower, nums[0] - 1])
        for prev_val, next_val in pairwise(nums):
            if next_val - prev_val > 1:
                result.append([prev_val + 1, next_val - 1])
        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])
        return result
