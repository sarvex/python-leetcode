class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        """Maximize sum of pair minimums by sorting and taking every other element.

        Intuition:
            To maximize the sum of min(a, b) for all pairs, we should pair
            adjacent elements after sorting so the smaller values lose the
            least possible.

        Approach:
            1. Sort the array.
            2. Sum elements at even indices (the minimum of each pair).

        Complexity:
            Time: O(n log n)
            Space: O(n) for sorting
        """
        nums.sort()
        return sum(nums[::2])
