from collections import Counter
from math import inf


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        """Sliding window over merged sorted elements to find smallest range.

        Intuition:
        Flatten all lists into tagged elements, sort them, then use a sliding window
        to find the smallest range that includes at least one element from each list.

        Approach:
        1. Create tagged tuples (value, list_index) from all lists and sort by value.
        2. Use a sliding window with a counter to track how many lists are covered.
        3. When all lists are covered, try to shrink the window from the left.
        4. Track the smallest range seen during the shrinking step.

        Complexity:
        Time: O(N log N) where N is total number of elements
        Space: O(N)
        """
        tagged = [
            (value, list_idx)
            for list_idx, values in enumerate(nums)
            for value in values
        ]
        tagged.sort()
        count = Counter()
        result = [-inf, inf]
        left = 0
        for right, (right_val, list_id) in enumerate(tagged):
            count[list_id] += 1
            while len(count) == len(nums):
                left_val = tagged[left][0]
                gap_diff = right_val - left_val - (result[1] - result[0])
                if gap_diff < 0 or (gap_diff == 0 and left_val < result[0]):
                    result = [left_val, right_val]
                left_list_id = tagged[left][1]
                count[left_list_id] -= 1
                if count[left_list_id] == 0:
                    count.pop(left_list_id)
                left += 1
        return result
