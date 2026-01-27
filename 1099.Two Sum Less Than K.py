from bisect import bisect_left


class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        """Find maximum pair sum less than k using sort and binary search.

        Intuition:
            After sorting, for each element we can binary search for the largest
            complement that keeps the sum below k.

        Approach:
            Sort the array. For each element at index i, binary search for the
            largest value in nums[i+1:] that is strictly less than k - nums[i].
            Track the maximum valid sum found.

        Complexity:
            Time: O(n log n) for sorting and binary searches
            Space: O(1) excluding sort space
        """
        nums.sort()
        result = -1
        for i, value in enumerate(nums):
            j = bisect_left(nums, k - value, lo=i + 1) - 1
            if i < j:
                result = max(result, value + nums[j])
        return result
