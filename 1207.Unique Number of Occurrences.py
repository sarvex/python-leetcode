from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Frequency Set Comparison - Check if all occurrence counts are unique

        Intuition:
        For occurrences to be unique, each number must appear a different number of times.
        We need to check if there are any duplicate occurrence counts.

        Approach:
        1. Count occurrences of each number using Counter
        2. Extract the occurrence values into a set
        3. Check if the number of unique occurrence values equals the number of unique elements
           - If equal, all occurrences are unique
           - If not equal, there are duplicate occurrence counts

        Complexity:
        Time: O(n) where n is the length of arr
        Space: O(k) where k is the number of unique elements in arr
        """
        counter = Counter(arr)
        values = list(counter.values())
        return len(set(values)) == len(values)
