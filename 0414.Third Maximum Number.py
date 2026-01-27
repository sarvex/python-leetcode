from math import inf


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        """Track three distinct maximums in a single pass.

        Intuition:
            Maintain three variables for the top three distinct values.
            Skip duplicates and shift values down as new maximums are found.

        Approach:
            1. Initialize three maximums to negative infinity.
            2. For each number, skip if already one of the three.
            3. Update the three maximums by shifting appropriately.
            4. Return the third max if it exists, otherwise return the first.

        Complexity:
            Time: O(n) for a single pass through nums.
            Space: O(1) using only three variables.
        """
        first_max = second_max = third_max = -inf
        for num in nums:
            if num in [first_max, second_max, third_max]:
                continue
            if num > first_max:
                third_max, second_max, first_max = second_max, first_max, num
            elif num > second_max:
                third_max, second_max = second_max, num
            elif num > third_max:
                third_max = num
        return third_max if third_max != -inf else first_max
