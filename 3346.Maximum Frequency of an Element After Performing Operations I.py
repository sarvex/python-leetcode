class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        Optimized sliding window approach with prefix sums
        
        Intuition:
        - Sort the array to easily calculate the number of operations needed
        - Use a sliding window to find the maximum frequency of any element
        - Calculate the operations needed to make all elements in the window equal to the rightmost element
        
        Approach:
        1. Sort the array to bring similar numbers together
        2. Use a sliding window [left, right] to track the current subarray
        3. Calculate the total operations needed to make all elements in the window equal to nums[right]
        4. If operations needed exceed k, move the left pointer to maintain the window
        5. Update the maximum frequency found so far
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) as we use constant extra space
        """
        nums.sort()
        left = 0
        total_operations = 0
        max_freq = 0
        
        for right in range(len(nums)):
            # The operations needed to make all elements up to right equal to nums[right]
            total_operations += (nums[right] - nums[(left + right) // 2])
            
            # If operations exceed k, move left pointer
            while total_operations > k:
                total_operations -= (nums[(left + right) // 2] - nums[left])
                left += 1
            
            # Update maximum frequency
            max_freq = max(max_freq, right - left + 1)
        
        return min(max_freq + numOperations, len(nums))
