class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """Sort-and-interleave approach for wiggle arrangement.

        Intuition:
            By sorting and placing smaller half at even indices (reversed) and
            larger half at odd indices (reversed), we guarantee the wiggle property.

        Approach:
            1. Sort the array into a temporary copy.
            2. Place elements from the middle of sorted array at even indices,
               counting downward.
            3. Place elements from the end of sorted array at odd indices,
               counting downward.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for the sorted copy
        """
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        mid_idx, end_idx = (length - 1) >> 1, length - 1
        for k in range(length):
            if k % 2 == 0:
                nums[k] = sorted_nums[mid_idx]
                mid_idx -= 1
            else:
                nums[k] = sorted_nums[end_idx]
                end_idx -= 1
