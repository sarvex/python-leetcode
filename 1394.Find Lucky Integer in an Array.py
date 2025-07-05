from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """Find the largest lucky integer in the array.

        Intuition: Count frequency of each number and find numbers that equal their frequency

        Approach: Use Counter to get frequency of each number, then find the largest number
        that appears exactly as many times as its value.

        Complexity:
            Time: O(n), where n is the length of the array
            Space: O(n), for storing the counter dictionary
        """
        counter = Counter(arr)

        # Find the largest lucky integer (or -1 if none exists)
        return max((num for num, freq in counter.items() if num == freq), default=-1)
