from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """Find the length of the longest nice subarray using sliding window with bitwise operations.

        Intuition:
        A nice subarray has no two elements with overlapping bits (bitwise AND = 0).
        We can use a sliding window approach where we maintain a bitmask of all
        bits used in the current window. When a new element conflicts with existing
        bits, we shrink the window from the left until no conflict exists.

        Approach:
        1. Use sliding window with two pointers (left and right)
        2. Maintain a bitmask representing all bits used in current window
        3. For each new element, check if it conflicts with existing bits
        4. If conflict exists, remove elements from left until conflict resolves
        5. Update maximum length and add current element to window

        Complexity:
        - Time: O(n) - each element is added and removed at most once
        - Space: O(1) - only using constant extra space for variables

        Args:
            nums: List of positive integers

        Returns:
            Length of the longest nice subarray
        """
        max_length = 0
        left = 0
        used_bits = 0

        for right, current_num in enumerate(nums):
            # Shrink window while current number conflicts with used bits
            while used_bits & current_num:
                used_bits ^= nums[left]
                left += 1

            # Update maximum length and add current number to window
            max_length = max(max_length, right - left + 1)
            used_bits |= current_num

        return max_length
