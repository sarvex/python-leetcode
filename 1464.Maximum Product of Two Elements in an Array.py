class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """Find maximum (nums[i]-1)*(nums[j]-1) for distinct indices.

        Intuition:
            The maximum product comes from the two largest elements in the array.

        Approach:
            Enumerate all pairs of distinct indices and compute the product
            of (a-1)*(b-1), tracking the maximum.

        Complexity:
            Time: O(n^2)
            Space: O(1)
        """
        result = 0
        for i, a in enumerate(nums):
            for b in nums[i + 1 :]:
                result = max(result, (a - 1) * (b - 1))
        return result
