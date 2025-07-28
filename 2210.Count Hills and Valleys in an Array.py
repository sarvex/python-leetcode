from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """Optimized monotonic traversal for hill and valley counting.

        Intuition:
        Instead of checking each position individually, traverse the array
        in monotonic segments. Each direction change (increasing to decreasing
        or vice versa) indicates a hill or valley.

        Approach:
        Skip initial plateaus, then traverse in monotonic segments.
        When direction changes from increasing to decreasing (or vice versa),
        we've found a hill or valley. Count these transition points.

        Complexity:
        Time: O(n) - single pass with optimized traversal
        Space: O(1) - only using constant extra space
        """
        array_length = len(nums)
        if array_length < 3:
            return 0

        hill_valley_count = 0
        current_index = 1

        # Skip initial plateau
        while current_index < array_length and nums[current_index] == nums[current_index - 1]:
            current_index += 1

        # If entire array is a plateau
        if current_index == array_length:
            return 0

        previous_value = nums[current_index - 1]

        while current_index < array_length:
            current_value = nums[current_index]

            if current_value > previous_value:
                # Traverse increasing segment
                while (current_index < array_length and
                       nums[current_index] >= previous_value):
                    previous_value = nums[current_index]
                    current_index += 1

                # Found peak (hill) if not at end
                if current_index < array_length:
                    hill_valley_count += 1

            elif current_value < previous_value:
                # Traverse decreasing segment
                while (current_index < array_length and
                       nums[current_index] <= previous_value):
                    previous_value = nums[current_index]
                    current_index += 1

                # Found valley if not at end
                if current_index < array_length:
                    hill_valley_count += 1

        return hill_valley_count
