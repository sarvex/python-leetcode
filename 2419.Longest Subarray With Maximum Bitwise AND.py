from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Find the length of the longest subarray with maximum bitwise AND value.

        Intuition:
        The maximum bitwise AND of any subarray will be the maximum element in the array.
        This is because AND operations can only decrease or maintain values, never increase them.
        So we need to find the longest contiguous sequence of the maximum element.

        Approach:
        1. Find the maximum value in the array
        2. Use a sliding window approach to track the longest contiguous sequence of the maximum value
        3. Keep track of current consecutive count and maximum consecutive count

        Complexity:
        - Time complexity: O(n) where n is the length of nums
        - Space complexity: O(1) only using constant extra space
        """
        # Find the maximum value in the array
        max_value = max(nums)
        # Track the maximum length of consecutive max_value elements
        max_length = 0
        current_length = 0
        # Iterate through the array to find longest contiguous sequence
        for num in nums:
            if num == max_value:
                # Extend current sequence
                current_length += 1
                # Update maximum if current is longer
                max_length = max(max_length, current_length)
            else:
                # Reset current sequence when we encounter a different value
                current_length = 0
        return max_length
