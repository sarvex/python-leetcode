from bisect import bisect_left


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """Count how many numbers are smaller than each element.

        Intuition:
            Sorting the array lets us use binary search to find how many
            elements are strictly less than a given value.

        Approach:
            Create a sorted copy and for each original element use bisect_left
            to find the count of strictly smaller values.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        sorted_nums = sorted(nums)
        return [bisect_left(sorted_nums, x) for x in nums]
