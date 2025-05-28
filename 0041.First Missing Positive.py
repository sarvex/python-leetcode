from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        In-place array manipulation to find the first missing positive integer.
        
        Intuition:
        The first missing positive must be in range [1, n+1] where n is array length.
        If we could somehow mark the presence of each positive number from 1 to n,
        we could find the first missing one by scanning through this information.
        
        Approach:
        1. Use the array itself as a hash table by placing each number at its
           corresponding index (nums[i] should be at index nums[i]-1).
        2. Iterate through the array and swap numbers to their correct positions
           when possible (1 ≤ nums[i] ≤ n).
        3. Scan the modified array - the first position where the number doesn't
           match its index+1 is our answer.
        4. If all numbers are in correct positions, the answer is n+1.
        
        Complexity:
        Time: O(n) - we scan the array twice and each element is moved at most once
        Space: O(1) - we use constant extra space regardless of input size
        """
        n = len(nums)
        
        # Place each number in its correct position
        for i in range(n):
            # Keep swapping until current position has correct number or invalid number
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Swap nums[i] with the number at its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Find the first position where the number doesn't match its index+1
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        
        # All numbers from 1 to n are present, so the answer is n+1
        return n + 1
