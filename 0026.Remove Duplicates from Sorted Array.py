from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two-pointer approach to remove duplicates in-place

        Intuition:
        Since the array is already sorted, duplicates will be adjacent. We can use
        a two-pointer technique where one pointer (k) keeps track of the position
        to place the next unique element, while iterating through the array with
        another pointer.

        Approach:
        1. Use a pointer k to track the position for the next unique element
        2. Iterate through the array with a second pointer
        3. When we find a unique element (different from the previous one), place it at position k
        4. Increment k to prepare for the next unique element
        5. Return k as the new length of the array with unique elements

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we modify the array in-place with constant extra space
        """
        if not nums:
            return 0

        insert = 0
        for num in nums:
            if insert == 0 or num != nums[insert - 1]:
                nums[insert] = num
                insert += 1
        return insert
