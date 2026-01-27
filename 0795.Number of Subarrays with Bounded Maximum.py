class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """Count subarrays with bounded max using inclusion-exclusion.

        Intuition:
            Count subarrays where max <= right minus subarrays where max <= left-1
            gives subarrays with max in [left, right].

        Approach:
            1. Define a helper that counts subarrays where all elements <= bound.
            2. For each element, extend the current valid subarray or reset.
            3. Return count_at_most(right) - count_at_most(left - 1).

        Complexity:
            Time: O(n)
            Space: O(1)
        """

        def count_at_most(bound: int) -> int:
            count = current_length = 0
            for value in nums:
                current_length = 0 if value > bound else current_length + 1
                count += current_length
            return count

        return count_at_most(right) - count_at_most(left - 1)
