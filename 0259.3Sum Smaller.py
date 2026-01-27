class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        """Two-pointer technique after sorting to count triplets with sum less than target.

        Intuition:
            Sorting allows us to use a two-pointer approach for each fixed element,
            efficiently counting all valid pairs without checking every combination.

        Approach:
            1. Sort the array.
            2. For each index i, use two pointers (left, right) on the remaining subarray.
            3. If the triplet sum is less than target, all pairs between left and right
               are valid, so add (right - left) to the count and advance left.
            4. Otherwise, decrement right to reduce the sum.

        Complexity:
            Time: O(n^2) where n is the length of nums
            Space: O(1) ignoring the sort space
        """
        nums.sort()
        count, length = 0, len(nums)
        for i in range(length):
            left, right = i + 1, length - 1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum >= target:
                    right -= 1
                else:
                    count += right - left
                    left += 1
        return count
