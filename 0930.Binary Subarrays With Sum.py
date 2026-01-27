from collections import Counter


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """Prefix sum with hash map counting for target subarray sum.

        Intuition:
            A subarray sums to the goal if the difference between two prefix
            sums equals the goal. We can count prefix sums using a hash map.

        Approach:
            1. Maintain a running prefix sum.
            2. For each new prefix sum, count how many previous prefix sums
               equal (current_sum - goal).
            3. Add the current prefix sum to the frequency map.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        prefix_count: Counter[int] = Counter({0: 1})
        result = prefix_sum = 0
        for value in nums:
            prefix_sum += value
            result += prefix_count[prefix_sum - goal]
            prefix_count[prefix_sum] += 1
        return result
