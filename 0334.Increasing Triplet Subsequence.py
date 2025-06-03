from typing import List
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Two-pointer greedy approach

        Intuition:
        Keep track of the smallest and second smallest values seen so far.
        If we find a value larger than both, we have our triplet.

        Approach:
        1. Initialize two variables to track the smallest (first) and second smallest (second) values
        2. Iterate through the array
        3. If current number is greater than second, we found our triplet
        4. If current number is less than or equal to first, update first
        5. Otherwise, update second

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we only use two variables regardless of input size
        """
        first, second = inf, inf

        for num in nums:
            if num > second:
                return True
            if num <= first:
                first = num
            else:
                second = num

        return False
