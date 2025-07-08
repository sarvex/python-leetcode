from typing import List
from collections import Counter


class FindSumPairs:
    """Hash map-based solution for finding pairs with a certain sum

    Intuition:
    Use frequency counters to efficiently track elements in both arrays and
    calculate pairs that sum to a target value.

    Approach:
    1. Store nums1 and nums2 frequencies in separate counters
    2. For add operation, update the frequency counter for nums2
    3. For count operation, iterate through nums1 frequencies and find matching pairs
       using the property that if a + b = tot, then b = tot - a

    Complexity:
    Time: O(n) for initialization, O(1) for add, O(k) for count where k is unique values in nums1
    Space: O(n + m) where n and m are the lengths of nums1 and nums2
    """

    def __init__(self, nums1: List[int], nums2: List[int]) -> None:
        """Initialize the FindSumPairs with two integer arrays.

        Args:
            nums1: First array of integers
            nums2: Second array of integers
        """
        self.nums2 = nums2
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        """Add val to nums2[index].

        Args:
            index: Index of the element to modify in nums2
            val: Value to add to the element
        """
        # Update frequency counter for the old value
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]

        # Update the value and frequency counter
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        """Count the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

        Args:
            tot: Target sum to find

        Returns:
            Number of pairs that sum to tot
        """
        return sum(count1 * self.freq2.get(tot - num1, 0)
                  for num1, count1 in self.freq1.items())


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index, val)
# param_2 = obj.count(tot)
