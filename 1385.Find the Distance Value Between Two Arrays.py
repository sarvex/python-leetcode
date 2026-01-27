from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """Count elements in arr1 with no arr2 element within distance d.

        Intuition:
            For each element in arr1, we need to check if any element in arr2
            is within distance d. Sorting arr2 and using binary search makes
            this efficient.

        Approach:
            Sort arr2. For each element a in arr1, use bisect_left to find
            the insertion point for a-d. If no element in arr2 falls within
            [a-d, a+d], count it.

        Complexity:
            Time: O((m + n) log n) where m = len(arr1) and n = len(arr2).
            Space: O(n) for sorting.
        """

        def is_distant(value: int) -> bool:
            idx = bisect_left(arr2, value - d)
            return idx == len(arr2) or arr2[idx] > value + d

        arr2.sort()
        return sum(is_distant(a) for a in arr1)
