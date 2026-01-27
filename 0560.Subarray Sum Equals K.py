from collections import Counter


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """Count subarrays with sum k using prefix sum and hash map.

        Intuition:
            If prefix_sum[j] - prefix_sum[i] == k, the subarray from i+1 to j
            sums to k. We count how many previous prefix sums equal current - k.

        Approach:
            1. Maintain a running prefix sum and a counter of seen prefix sums.
            2. For each element, add prefix_sum - k occurrences to the answer.
            3. Increment the count of the current prefix sum.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        prefix_count = Counter({0: 1})
        answer = prefix_sum = 0
        for num in nums:
            prefix_sum += num
            answer += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1
        return answer
