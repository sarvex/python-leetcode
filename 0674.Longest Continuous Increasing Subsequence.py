class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        """Single pass tracking current streak length of increasing elements.

        Intuition:
        Scan left to right, extending the current streak when elements increase,
        resetting otherwise. Track the maximum streak seen.

        Approach:
        1. Initialize both answer and current count to 1.
        2. For each consecutive pair, if increasing, extend count and update max.
        3. Otherwise reset count to 1.

        Complexity:
        Time: O(n)
        Space: O(1)
        """
        max_length = current_length = 1
        for i, value in enumerate(nums[1:]):
            if nums[i] < value:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1
        return max_length
