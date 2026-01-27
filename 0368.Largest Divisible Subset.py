class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        """Find largest divisible subset using dynamic programming.

        Intuition:
            If we sort the array, a divisible subset forms a chain where each
            element divides the next. This is similar to longest increasing
            subsequence but with divisibility.

        Approach:
            Sort the array. Use DP where dp[i] stores the length of the largest
            divisible subset ending at index i. For each pair (i, j) where j < i,
            if nums[i] % nums[j] == 0, update dp[i]. Track the index of the
            maximum dp value. Reconstruct the subset by backtracking from that
            index, collecting elements that satisfy divisibility and matching
            dp values.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        nums.sort()
        length = len(nums)
        dp = [1] * length
        best_idx = 0
        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[best_idx] < dp[i]:
                best_idx = i
        remaining = dp[best_idx]
        current = best_idx
        result: list[int] = []
        while remaining:
            if nums[best_idx] % nums[current] == 0 and dp[current] == remaining:
                result.append(nums[current])
                best_idx, remaining = current, remaining - 1
            current -= 1
        return result
