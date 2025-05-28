from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays using binary search.
        
        Intuition:
        The median divides the combined array into two equal halves. We can find this partition
        by performing binary search on the smaller array to find the correct split point.
        
        Approach:
        1. Ensure nums1 is the smaller array to minimize binary search space
        2. Use binary search to find the partition point in nums1
        3. Calculate the corresponding partition in nums2
        4. Check if we've found the correct partition where all left elements are <= right elements
        5. Calculate the median based on whether the total length is even or odd
        
        Complexity:
        Time: O(log(min(m,n))) where m and n are lengths of nums1 and nums2
        Space: O(1) - constant extra space is used
        """
        # Ensure nums1 is the smaller array to reduce binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # +1 to handle both even and odd lengths
        
        # Binary search on the smaller array (nums1)
        left, right = 0, m
        while left <= right:
            # Partition nums1
            i = (left + right) // 2  # mid point in nums1
            # Calculate corresponding partition in nums2
            j = half - i
            
            # Handle out of bounds cases
            nums1_left = float('-inf') if i == 0 else nums1[i-1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j-1]
            nums2_right = float('inf') if j == n else nums2[j]
            
            # Check if we've found the correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Calculate median based on even or odd total length
                if total % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    left_max = max(nums1_left, nums2_left)
                    right_min = min(nums1_right, nums2_right)
                    return (left_max + right_min) / 2
            elif nums1_left > nums2_right:
                # Move partition left in nums1
                right = i - 1
            else:
                # Move partition right in nums1
                left = i + 1
                
        # This line should never be reached with valid input
        raise ValueError("Input arrays are not sorted")
