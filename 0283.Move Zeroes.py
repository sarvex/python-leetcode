from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Fill-and-overwrite approach to move zeroes to the end

        Intuition:
        First collect all non-zero elements at the beginning of the array,
        then fill the remaining positions with zeroes.

        Approach:
        1. Use a pointer to track the position for the next non-zero element
        2. Iterate through the array, placing non-zero elements at the pointer position
        3. After all non-zero elements are placed, fill the rest with zeroes

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we modify the array in-place with no extra space
        """
        pos = 0
        # First pass: move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1

        # Second pass: fill remaining positions with zeroes
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
