class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """Cyclic sort to place each number at its correct index, then find mismatches.

        Intuition:
            Since values are in [1, n], each value v should be at index v-1.
            After sorting in-place, any position where nums[i] != i+1 indicates
            a duplicate.

        Approach:
            1. For each index, swap nums[i] to its correct position nums[i]-1
               until it's already there or matches.
            2. After sorting, collect values where nums[i] != i+1.

        Complexity:
            Time: O(n) since each element is swapped at most once.
            Space: O(1) excluding the output list (in-place swaps).
        """
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [value for i, value in enumerate(nums) if value != i + 1]
