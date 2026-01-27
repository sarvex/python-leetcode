from itertools import pairwise
from math import inf


class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        """Maximize array value after reversing exactly one subarray.

        Intuition:
            The array value is the sum of |nums[i] - nums[i+1]|. Reversing a
            subarray only changes boundary pairs. Analyze edge reversals and
            interior reversals separately using sign analysis.

        Approach:
            First compute the base sum. Check reversals touching index 0 or n-1.
            For interior reversals, use the four sign combinations to find the
            maximum gain from swapping boundary contributions.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        base_sum = sum(abs(x - y) for x, y in pairwise(nums))
        best = base_sum
        for x, y in pairwise(nums):
            best = max(best, base_sum + abs(nums[0] - y) - abs(x - y))
            best = max(best, base_sum + abs(nums[-1] - x) - abs(x - y))
        for sign_a, sign_b in pairwise((1, -1, -1, 1, 1)):
            max_val = -inf
            min_val = inf
            for x, y in pairwise(nums):
                contribution = sign_a * x + sign_b * y
                diff = abs(x - y)
                max_val = max(max_val, contribution - diff)
                min_val = min(min_val, contribution + diff)
            best = max(best, base_sum + max(max_val - min_val, 0))
        return best
