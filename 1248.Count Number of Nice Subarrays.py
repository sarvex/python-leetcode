from collections import Counter


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """Count subarrays with exactly k odd numbers using prefix sum.

        Intuition:
            Transform the problem into counting subarrays with a specific sum by
            treating each element as 1 (odd) or 0 (even). Then use the prefix sum
            technique with a hash map to count valid subarrays.

        Approach:
            Maintain a running prefix count of odd numbers. For each position, the
            number of valid subarrays ending here equals the count of previous
            prefix sums that equal (current_prefix - k).

        Complexity:
            Time: O(n) — single pass through the array
            Space: O(n) — for the prefix count hash map
        """
        prefix_count = Counter({0: 1})
        result = 0
        odd_count = 0
        for value in nums:
            odd_count += value & 1
            result += prefix_count[odd_count - k]
            prefix_count[odd_count] += 1
        return result
