from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """Find longest subarray where max - min <= limit using sorted list.

        Intuition:
            Use a sliding window with a sorted container to efficiently track
            the current min and max values.

        Approach:
            Maintain a SortedList for the current window. Expand the right end
            by adding elements. When the difference between max and min exceeds
            the limit, shrink from the left. Track the maximum window size.

        Complexity:
            Time: O(n log n) for sorted list operations
            Space: O(n) for the sorted list
        """
        sorted_window = SortedList()
        result = left = 0
        for right, value in enumerate(nums):
            sorted_window.add(value)
            while sorted_window[-1] - sorted_window[0] > limit:
                sorted_window.remove(nums[left])
                left += 1
            result = max(result, right - left + 1)
        return result
