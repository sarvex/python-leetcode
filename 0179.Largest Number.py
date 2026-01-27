from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """Custom Sort Comparator Approach

        Intuition:
            To form the largest number, compare two numbers by their
            concatenation order: a+b vs b+a.

        Approach:
            1. Convert all integers to strings.
            2. Sort using a custom comparator that compares a+b vs b+a.
            3. Join the sorted strings; handle the edge case where the
               result is all zeros.

        Complexity:
            Time: O(n log n) for sorting with custom comparator
            Space: O(n) for the string conversion list
        """
        str_nums = [str(v) for v in nums]
        str_nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return "0" if str_nums[0] == "0" else "".join(str_nums)
