class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        """Greedy approach on sorted array with split point enumeration.

        Intuition:
            After sorting, the optimal strategy is to increase smaller elements
            by k and decrease larger elements by k. The split point determines
            which elements go up and which go down.

        Approach:
            1. Sort the array.
            2. The initial answer is max - min (no changes).
            3. For each split point, compute the new min and max considering
               elements before the split are increased by k and elements after
               are decreased by k.
            4. Return the minimum range found.

        Complexity:
            Time: O(n log n)
            Space: O(1)
        """
        nums.sort()
        result = nums[-1] - nums[0]
        for idx in range(1, len(nums)):
            min_val = min(nums[0] + k, nums[idx] - k)
            max_val = max(nums[idx - 1] + k, nums[-1] - k)
            result = min(result, max_val - min_val)
        return result
