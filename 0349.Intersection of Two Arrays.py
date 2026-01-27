class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Set intersection for unique common elements.

        Intuition:
            Converting both arrays to sets and using the intersection operator
            gives unique common elements directly.

        Approach:
            1. Convert both lists to sets.
            2. Return the set intersection as a list.

        Complexity:
            Time: O(n + m) where n and m are the lengths of the arrays
            Space: O(n + m) for the sets
        """
        return list(set(nums1) & set(nums2))
