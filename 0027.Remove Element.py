from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two-pointer approach for in-place element removal
        
        Intuition:
        Use a two-pointer technique where one pointer (k) tracks the position for 
        the next non-matching element, while we iterate through the array with 
        another implicit pointer.
        
        Approach:
        1. Initialize a pointer k to track the position where the next non-matching 
           element should be placed
        2. Iterate through each element in the array
        3. If the current element doesn't match the target value, place it at 
           position k and increment k
        4. Return k as the new length of the array with target values removed
        
        Complexity:
        Time: O(n) where n is the length of nums, as we process each element once
        Space: O(1) as we modify the array in-place without extra space
        """
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k
