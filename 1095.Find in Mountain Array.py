# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        """Find target in mountain array using binary search.

        Intuition:
            A mountain array has a single peak. First locate the peak via binary
            search, then search the ascending side, and if not found, search the
            descending side.

        Approach:
            Binary search for the peak where arr[mid] > arr[mid+1]. Then binary
            search the ascending half (left of peak) and descending half (right
            of peak) using a direction multiplier to unify the comparison logic.

        Complexity:
            Time: O(log n) for three binary searches
            Space: O(1)
        """

        def binary_search(left: int, right: int, direction: int) -> int:
            while left < right:
                mid = (left + right) >> 1
                if direction * mountain_arr.get(mid) >= direction * target:
                    right = mid
                else:
                    left = mid + 1
            return -1 if mountain_arr.get(left) != target else left

        length = mountain_arr.length()
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) >> 1
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        peak = left
        ascending_result = binary_search(0, peak, 1)
        return (
            binary_search(peak + 1, length - 1, -1)
            if ascending_result == -1
            else ascending_result
        )
