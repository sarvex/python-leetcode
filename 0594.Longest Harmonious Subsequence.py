from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """Frequency counting approach for finding the longest harmonious subsequence.

        Intuition:
        A harmonious array contains exactly two distinct integers with a difference of 1.
        By counting frequencies of each number, we can find pairs of adjacent numbers
        and calculate the length of their combined subsequence.

        Approach:
        1. Count the frequency of each number in the input array
        2. For each number x in the counter, check if x+1 also exists
        3. If it does, calculate the combined length of subsequences with x and x+1
        4. Return the maximum combined length found

        Complexity:
        Time: O(n) where n is the length of nums (single pass through the array)
        Space: O(k) where k is the number of distinct integers in nums
        """
        # Count frequency of each number and use generator expression for pythonic solution
        counter = Counter(nums)
        return max((c + counter[x + 1] for x, c in counter.items() if counter[x + 1]), default=0)
