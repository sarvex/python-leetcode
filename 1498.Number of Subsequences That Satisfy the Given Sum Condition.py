from typing import List
from bisect import bisect_right


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """Two pointers with binary search approach.

        Intuition:
        For each minimum value in a subsequence, we need to find all valid maximum values
        that satisfy min + max ≤ target. Since order doesn't matter in subsequences,
        we can sort the array and use binary search to efficiently find these values.

        Approach:
        1. Sort the array to easily identify min and max values
        2. Precompute powers of 2 for subsequence counting
        3. For each potential minimum value, find the maximum valid index using binary search
        4. Calculate number of valid subsequences using 2^(j-i) formula

        Complexity:
        Time: O(n log n) due to sorting and binary search operations
        Space: O(n) for storing powers of 2
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2 for subsequence counting
        powers = [1] + [0] * n
        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * 2) % MOD

        result = 0
        for i, min_val in enumerate(nums):
            # Early termination if minimum value alone exceeds half of target
            if min_val * 2 > target:
                break

            # Find the rightmost index j where nums[j] <= target - min_val
            j = bisect_right(nums, target - min_val, i + 1) - 1

            # Add number of valid subsequences with nums[i] as minimum
            # 2^(j-i) represents all possible ways to select elements between i and j
            result = (result + powers[j - i]) % MOD

        return result
