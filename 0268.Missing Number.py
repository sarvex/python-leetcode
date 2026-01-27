from functools import reduce
from operator import xor


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """XOR all indices and values to find the missing number.

        Intuition:
            XOR of a number with itself is 0. By XORing all indices [1..n] with
            all values in the array, all paired numbers cancel out, leaving only
            the missing number.

        Approach:
            1. Enumerate nums starting from index 1 to create pairs (i, v).
            2. XOR each index with its corresponding value.
            3. Reduce all XOR results to get the missing number.

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(1)
        """
        return reduce(xor, (i ^ v for i, v in enumerate(nums, 1)))
