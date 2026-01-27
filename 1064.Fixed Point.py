class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        """Find the smallest index where arr[i] == i.

        Intuition:
            Since the array is sorted with distinct values, binary search for
            the leftmost fixed point.

        Approach:
            Binary search: if arr[mid] >= mid, the answer could be at mid or
            left; otherwise search right.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] >= mid:
                right = mid
            else:
                left = mid + 1
        return left if arr[left] == left else -1
