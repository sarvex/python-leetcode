from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        One-pass counter approach for finding maximum number of k-sum pairs.

        Intuition:
        Instead of sorting and using two pointers, we can use a counter to track
        frequencies of numbers we've seen so far. For each number, check if its
        complement (k - num) exists in our counter.

        Approach:
        1. Use a Counter to track frequencies of numbers
        2. For each number, check if (k - num) exists in counter
        3. If it does, pair them and decrement the counter
        4. Count total pairs formed

        Complexity:
        Time: O(n) where n is the length of nums
        Space: O(n) for storing the counter
        """
        counter = Counter()
        operations = 0

        for num in nums:
            complement = k - num
            if counter[complement] > 0:
                counter[complement] -= 1
                operations += 1
            else:
                counter[num] += 1

        return operations
