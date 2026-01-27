from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        """Bit manipulation using XOR and lowest set bit to separate two unique numbers.

        Intuition:
            XOR of all numbers gives the XOR of the two unique numbers. The lowest
            set bit in this result differentiates the two numbers, allowing us to
            partition all numbers into two groups.

        Approach:
            1. XOR all numbers to get combined_xor = a ^ b.
            2. Find the lowest set bit of combined_xor to use as a separator.
            3. XOR all numbers that have this bit set to isolate one unique number.
            4. XOR the result with combined_xor to get the other unique number.

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(1)
        """
        combined_xor = reduce(xor, nums)
        first_unique = 0
        lowest_set_bit = combined_xor & -combined_xor
        for num in nums:
            if num & lowest_set_bit:
                first_unique ^= num
        second_unique = combined_xor ^ first_unique
        return [first_unique, second_unique]
