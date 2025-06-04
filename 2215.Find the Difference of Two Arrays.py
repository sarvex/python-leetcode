from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """Set operations to find unique elements in each array.

        Intuition:
        When finding elements unique to each array, set operations are the most efficient
        approach as they provide O(1) lookups and built-in difference operations.

        Approach:
        1. Convert both input arrays to sets to remove duplicates
        2. Use set difference operations to find elements unique to each set
        3. Convert the resulting sets back to lists as required by the return type

        Complexity:
        Time: O(n + m) where n and m are the lengths of nums1 and nums2
        Space: O(n + m) for storing the sets and result lists
        """
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
