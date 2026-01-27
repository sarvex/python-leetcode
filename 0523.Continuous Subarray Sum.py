class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """Prefix sum modulo with hash map to find subarray divisible by k.

        Intuition:
            If two prefix sums have the same remainder mod k, then the subarray
            between them sums to a multiple of k.

        Approach:
            Track prefix sum mod k. Store the first index where each remainder
            appears. If the same remainder appears again with index gap > 1,
            return True.

        Complexity:
            Time: O(n)
            Space: O(min(n, k))
        """
        remainder_index = {0: -1}
        prefix_mod = 0
        for i, value in enumerate(nums):
            prefix_mod = (prefix_mod + value) % k
            if prefix_mod not in remainder_index:
                remainder_index[prefix_mod] = i
            elif i - remainder_index[prefix_mod] > 1:
                return True
        return False
