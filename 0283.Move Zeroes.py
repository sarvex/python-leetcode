from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Two-pointer approach to move all zeroes to the end while maintaining order

        Intuition:
        Use a two-pointer technique where one pointer tracks the position where
        the next non-zero element should go, and another pointer scans through
        the array to find non-zero elements.

        Approach:
        1. Initialize a pointer i at -1 to track where the next non-zero element should go
        2. Iterate through the array with pointer j
        3. When a non-zero element is found, increment i and swap elements at positions i and j
        4. This effectively moves all non-zero elements to the front while preserving their order
        5. All zeroes naturally end up at the end of the array

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we modify the array in-place with no extra space
        """
        i = -1
        for j, x in enumerate(nums):
            if x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

    def moveZeroes_alt(self, nums: List[int]) -> None:
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
