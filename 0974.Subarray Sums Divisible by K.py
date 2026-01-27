from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """Prefix sum modulo counting to find subarrays divisible by k.

        Intuition:
        If two prefix sums have the same remainder mod k, the subarray between
        them has a sum divisible by k. Counting remainder frequencies lets us
        compute valid pairs efficiently.

        Approach:
        1. Maintain a running prefix sum modulo k
        2. Use a counter to track how many times each remainder has appeared
        3. For each new remainder, add the count of previous same remainders

        Complexity:
        Time: O(n) where n is the array length
        Space: O(k) for the remainder counter
        """
        remainder_count = Counter({0: 1})
        result = 0
        prefix_mod = 0
        for num in nums:
            prefix_mod = (prefix_mod + num) % k
            result += remainder_count[prefix_mod]
            remainder_count[prefix_mod] += 1
        return result
