from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:
        """Sorted set with sliding window for range-based duplicate detection.

        Intuition:
            Maintain a sorted set of values within the index window. For each
            new element, binary search for any value within the allowed range.

        Approach:
            1. Use a sorted set to maintain values in the current window.
            2. For each value, find the leftmost element >= (value - valueDiff).
            3. If that element is also <= (value + valueDiff), return True.
            4. Slide the window by removing elements outside indexDiff.

        Complexity:
            Time: O(n log(min(n, indexDiff)))
            Space: O(min(n, indexDiff))
        """
        sorted_window: SortedSet = SortedSet()
        for idx, value in enumerate(nums):
            position = sorted_window.bisect_left(value - valueDiff)
            if (
                position < len(sorted_window)
                and sorted_window[position] <= value + valueDiff
            ):
                return True
            sorted_window.add(value)
            if idx >= indexDiff:
                sorted_window.remove(nums[idx - indexDiff])
        return False
