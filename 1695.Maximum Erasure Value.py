from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """Direct sliding window approach with running sum

        Intuition:
        Use a sliding window to track unique elements and maintain a running sum
        of the current window, adjusting when duplicates are found.

        Approach:
        1. Maintain a set to track unique elements in the current window
        2. Keep a running sum of elements in the current window
        3. When encountering a duplicate, shrink the window from the left until
           the duplicate is removed, updating the running sum accordingly
        4. Track the maximum sum seen so far

        Complexity:
        Time: O(n) where n is the length of nums
        Space: O(k) where k is the number of unique elements in nums
        """
        max_sum = 0        # Maximum sum found so far
        current_sum = 0    # Sum of current window
        num_set = set()    # Set to track unique elements in current window
        left = 0           # Left boundary of current window

        for num in nums:
            # If we encounter a duplicate
            if num in num_set:
                # Shrink window from left until duplicate is removed
                while nums[left] != num:
                    current_sum -= nums[left]  # Remove from sum
                    num_set.remove(nums[left])  # Remove from set
                    left += 1

                # Skip the duplicate element itself
                left += 1
            else:
                # Add new unique element to window
                num_set.add(num)
                current_sum += num

                # Update maximum sum if current is larger
                max_sum = max(max_sum, current_sum)

        return max_sum
