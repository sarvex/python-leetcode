from bisect import bisect_left
from math import ceil


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        """Find the smallest divisor such that the sum of divided values is at most threshold.

        Intuition:
            The sum of ceil(num/divisor) is monotonically non-increasing as divisor grows,
            so binary search finds the smallest valid divisor.

        Approach:
            Binary search over divisor values from 1 to max(nums). For each candidate,
            check if the sum of ceil divisions is within the threshold.

        Complexity:
            Time: O(n * log(max(nums)))
            Space: O(1)
        """

        def is_valid(divisor: int) -> bool:
            divisor += 1
            return sum(ceil(x / divisor) for x in nums) <= threshold

        return bisect_left(range(max(nums)), True, key=is_valid) + 1
