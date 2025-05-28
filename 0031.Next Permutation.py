from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        In-place next lexicographically greater permutation
        
        Intuition:
        The next permutation is the next lexicographically greater arrangement of elements.
        To find it, we need to find the first decreasing element from the right,
        swap it with the smallest element to its right that is greater than it,
        and then reverse the remaining elements to the right.
        
        Approach:
        1. Find the first decreasing element from the right (i)
        2. If found, find the smallest element to the right of i that is greater than nums[i]
        3. Swap these two elements
        4. Reverse the subarray to the right of position i
        5. If no decreasing element is found, the array is in descending order, so reverse it
        
        Complexity:
        Time: O(n) where n is the length of the array
        Space: O(1) as we modify the array in-place
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = next((i for i in range(n - 2, -1, -1) if nums[i] < nums[i + 1]), -1)
        
        # Step 2 & 3: If found, swap with the smallest element to the right that is greater
        if i != -1:  # Using explicit comparison instead of bitwise complement
            j = next((j for j in range(n - 1, i, -1) if nums[j] > nums[i]))
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 4: Reverse the subarray to the right of position i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
