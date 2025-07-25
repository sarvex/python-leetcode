from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Greedy selection of unique positive elements for maximum sum.
        
        Intuition:
        Since we can delete any elements, we should keep only positive unique
        elements to maximize the sum. Negative elements and duplicates should
        be removed.
        
        Approach:
        1. Handle edge case where all elements are non-positive
        2. Use a set to track seen elements and avoid duplicates
        3. Sum only positive unique elements
        
        Complexity:
        Time: O(n) - single pass through array
        Space: O(k) - set storage for unique positive elements
        """
        # Edge case: if maximum element is non-positive, return it
        max_element = max(nums)
        if max_element <= 0:
            return max_element
        
        return self._calculate_max_unique_sum(nums)
    
    def _calculate_max_unique_sum(self, nums: List[int]) -> int:
        """Calculate sum of unique positive elements."""
        seen_elements = set()
        total_sum = 0
        
        for num in nums:
            if self._should_include_element(num, seen_elements):
                total_sum += num
                seen_elements.add(num)
        
        return total_sum
    
    def _should_include_element(self, num: int, seen: set) -> bool:
        """Check if element should be included in the sum."""
        return num > 0 and num not in seen
