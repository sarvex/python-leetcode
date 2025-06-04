from typing import List
from itertools import accumulate


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Prefix Sum Tracking - Find maximum altitude by tracking cumulative height changes

Intuition:
        Starting at altitude 0, each value in the gain array represents a change in altitude.
        By calculating the running sum at each point, we can determine all altitudes visited.
        The highest altitude will be the maximum value among these running sums.

Approach:
        1. Use itertools.accumulate to calculate the running sum of altitude changes
        2. Include initial altitude of 0 using the initial parameter
        3. Return the maximum value from the resulting sequence

Complexity:
        Time: O(n) where n is the length of the gain array
        Space: O(n) for storing the accumulated values
        """
        return max(accumulate(gain, initial=0))
