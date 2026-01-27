class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        """Meet-in-the-middle with subset sums to check equal average split.

        Intuition:
            Normalize values so the problem becomes finding a non-empty proper
            subset summing to zero. Split the array in half and enumerate
            subsets for each half.

        Approach:
            1. Transform each value: nums[i] = nums[i] * n - total_sum.
            2. Enumerate all subset sums for the first half; store in a set.
            3. Enumerate all subset sums for the second half; check if
               complement exists (excluding the full array).

        Complexity:
            Time: O(2^(n/2))
            Space: O(2^(n/2))
        """
        length = len(nums)
        if length == 1:
            return False
        total = sum(nums)
        for i, value in enumerate(nums):
            nums[i] = value * length - total
        half = length >> 1
        first_half_sums: set[int] = set()
        for mask in range(1, 1 << half):
            subset_sum = sum(
                value for j, value in enumerate(nums[:half]) if mask >> j & 1
            )
            if subset_sum == 0:
                return True
            first_half_sums.add(subset_sum)
        for mask in range(1, 1 << (length - half)):
            subset_sum = sum(
                value for j, value in enumerate(nums[half:]) if mask >> j & 1
            )
            if subset_sum == 0 or (
                mask != (1 << (length - half)) - 1 and -subset_sum in first_half_sums
            ):
                return True
        return False
