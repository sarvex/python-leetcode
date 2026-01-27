from collections import Counter


class Solution:
    def arraysIntersection(
        self, arr1: list[int], arr2: list[int], arr3: list[int]
    ) -> list[int]:
        """Intersection of three sorted arrays.

        Intuition:
            An element appears in all three arrays if and only if its total
            count across the combined arrays is exactly 3.

        Approach:
            Concatenate all three arrays and count occurrences. Filter elements
            from arr1 that have a count of 3, preserving sorted order.

        Complexity:
            Time: O(n) where n is the total number of elements
            Space: O(n) for the counter
        """
        frequency = Counter(arr1 + arr2 + arr3)
        return [x for x in arr1 if frequency[x] == 3]
