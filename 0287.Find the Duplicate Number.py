from bisect import bisect_left


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """Binary search on value range with counting predicate.

        Intuition:
            For the duplicate value x, the count of numbers <= x in the array
            will exceed x. Binary search can find the smallest such x.

        Approach:
            1. Define a predicate: count of elements <= x exceeds x.
            2. Use bisect_left on the range [1, n] with this predicate.
            3. The first value where the predicate is True is the duplicate.

        Complexity:
            Time: O(n log n)
            Space: O(1)
        """

        def count_less_or_equal(value: int) -> bool:
            return sum(v <= value for v in nums) > value

        return bisect_left(range(len(nums)), True, key=count_less_or_equal)
