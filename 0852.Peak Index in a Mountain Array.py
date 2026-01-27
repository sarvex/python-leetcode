class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        """Binary search for the peak element in a mountain array.

        Intuition:
            The mountain array first increases then decreases. At any midpoint,
            comparing with the next element tells us which side the peak is on.

        Approach:
            1. Binary search between indices 1 and n-2
            2. If arr[mid] > arr[mid+1], peak is at mid or left
            3. Otherwise, peak is to the right

        Complexity:
            Time: O(log n) where n is the array length
            Space: O(1)
        """
        left, right = 1, len(arr) - 2
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
