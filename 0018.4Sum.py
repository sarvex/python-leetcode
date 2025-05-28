from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Two pointers with sorting approach for 4Sum problem.
        
        Intuition: Similar to 3Sum, we can fix two pointers and use two pointers technique
        to find pairs that sum up to the target. We need to handle duplicates carefully.
        
        Approach:
        1. Sort the array to handle duplicates and enable two-pointer technique
        2. Use two nested loops to fix the first two numbers
        3. Use two pointers for the remaining two numbers
        4. Skip duplicates at each level to avoid duplicate quadruplets
        5. Optimize by early termination when possible
        
        Complexity:
        Time: O(n³) where n is the length of the input array
        Space: O(1) excluding the output array
        """
        n = len(nums)
        result = []
        
        if n < 4:
            return result
            
        nums.sort()
        
        for i in range(n - 3):
            # Skip duplicates for first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Early termination if smallest possible sum > target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
                
            # Early skip if largest possible sum < target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for second position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Early termination check
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                    
                # Early skip if largest possible sum < target
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                    
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for third and fourth positions
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
        return result
