from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Frequency Set Comparison - Check if all occurrence counts are unique

        Intuition:
        If each number appears a unique number of times, then the set of
        occurrence counts should have the same size as the counter dictionary.

        Approach:
        1. Count occurrences of each number using Counter
        2. Extract the occurrence values into a set
        3. Compare the length of the set with the length of the counter
           - If equal, all occurrences are unique
           - If not equal, there are duplicate occurrence counts

        Complexity:
        Time: O(n) where n is the length of arr
        Space: O(k) where k is the number of unique elements in arr
        """
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter)
