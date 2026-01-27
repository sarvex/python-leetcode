class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """Sort arr1 such that elements appear in the relative order of arr2.

        Intuition:
            Elements in arr2 have a defined order; remaining elements should
            be sorted numerically and placed at the end.

        Approach:
            Create a position map from arr2. Sort arr1 using a custom key that
            maps arr2 elements to their index and unmapped elements to a value
            beyond arr2's range plus the element itself for numeric ordering.

        Complexity:
            Time: O(n log n) where n is the length of arr1
            Space: O(m) where m is the length of arr2 for the position map
        """
        position = {value: index for index, value in enumerate(arr2)}
        return sorted(arr1, key=lambda x: position.get(x, 1000 + x))
