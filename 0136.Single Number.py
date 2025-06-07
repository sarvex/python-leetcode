from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """XOR-based single number finder

        Intuition:
        When we XOR a number with itself, we get 0. When we XOR a number with 0,
        we get the number back. So if we XOR all numbers in the array, the duplicates
        will cancel out, leaving only the single number.

        Approach:
        Use the reduce function with XOR operation on the entire array. The duplicates
        will cancel each other out (a⊕a=0), and the single number will remain (a⊕0=a).

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we only use a constant amount of extra space
        """
        return reduce(xor, nums)
