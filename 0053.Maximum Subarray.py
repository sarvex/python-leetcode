from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm for Maximum Subarray

        Intuition:
        The key insight is that if a subarray's sum becomes negative, it's better to
        start fresh with the next element rather than carrying the negative sum forward.

        Approach:
        1. Initialize two variables: current_sum and max_sum with the first element
        2. Iterate through the array starting from the second element
        3. For each element, decide whether to start a new subarray (if current_sum < 0)
           or extend the existing subarray
        4. Update max_sum if the current_sum is greater
        5. Return max_sum after the iteration

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we only use two variables regardless of input size
        """
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            # Either start a new subarray or extend the existing one
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
