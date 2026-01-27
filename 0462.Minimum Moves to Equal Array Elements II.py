class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        """Sort and converge to the median element.

        Intuition:
            The median minimizes the sum of absolute deviations, making it
            the optimal target value.

        Approach:
            Sort the array, pick the median element, then sum the absolute
            differences between each element and the median.

        Complexity:
            Time: O(n log n) — dominated by sorting
            Space: O(1) — in-place sort
        """
        nums.sort()
        median = nums[len(nums) >> 1]
        return sum(abs(value - median) for value in nums)
