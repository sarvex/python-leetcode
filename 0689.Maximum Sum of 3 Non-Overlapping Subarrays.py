class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        """Sliding window tracking best single and double subarray sums.

        Intuition:
            Maintain three sliding windows simultaneously. Track the best
            single window sum and the best pair of windows as we slide the
            third window, updating the answer whenever the total improves.

        Approach:
            1. Use three sliding windows of size k each.
            2. Track the maximum single window sum and its index.
            3. Track the maximum combined two-window sum and their indices.
            4. For each position of the third window, check if adding it to
               the best two-window sum produces a new global maximum.

        Complexity:
            Time: O(n) single pass through the array
            Space: O(1) only tracking sums and indices
        """
        best_total = sum1 = sum2 = sum3 = 0
        max_sum1 = max_sum12 = 0
        best_idx1 = 0
        best_idx12: tuple[int, ...] = ()
        result: list[int] = []
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    best_idx1 = i - k * 3 + 1
                if max_sum1 + sum2 > max_sum12:
                    max_sum12 = max_sum1 + sum2
                    best_idx12 = (best_idx1, i - k * 2 + 1)
                if max_sum12 + sum3 > best_total:
                    best_total = max_sum12 + sum3
                    result = [*best_idx12, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return result
