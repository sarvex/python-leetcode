from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Sliding Window

        Intuition:
        Use a sliding window of size k to find the maximum average subarray.

        Approach:
        1. Calculate the sum of first k elements
        2. Slide the window by adding the next element and removing the first element
        3. Keep track of the maximum sum encountered
        4. Return the maximum sum divided by k

        Complexity:
        Time: O(n) where n is the length of nums
        Space: O(1) as we only use constant extra space
        """
        # Calculate initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window and update max_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
