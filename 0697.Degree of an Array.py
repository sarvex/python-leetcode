from collections import Counter
from math import inf


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """Find shortest subarray with the same degree as the full array.

        Intuition:
            The degree is the maximum frequency. The shortest subarray with
            that degree spans from the first to last occurrence of the most
            frequent element.

        Approach:
            1. Count frequencies and find the degree.
            2. Record first and last occurrence of each element.
            3. Among elements with frequency equal to degree, find the
               minimum span (last - first + 1).

        Complexity:
            Time: O(n) for counting and scanning
            Space: O(n) for the frequency and position dictionaries
        """
        frequency = Counter(nums)
        degree = frequency.most_common()[0][1]
        first_occurrence: dict[int, int] = {}
        last_occurrence: dict[int, int] = {}
        for i, value in enumerate(nums):
            if value not in first_occurrence:
                first_occurrence[value] = i
            last_occurrence[value] = i
        shortest = inf
        for value in nums:
            if frequency[value] == degree:
                span = last_occurrence[value] - first_occurrence[value] + 1
                if shortest > span:
                    shortest = span
        return shortest
