class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """Backtracking with pruning to partition array into k equal-sum subsets.

        Intuition:
            Try to fill k buckets each with target sum. Sorting in descending
            order and skipping duplicate bucket states prunes the search space.

        Approach:
            1. Compute target sum per bucket. Return False if total isn't
               divisible by k.
            2. Sort descending so larger numbers are placed first for early
               pruning.
            3. Use backtracking: try placing each number into a bucket. Skip
               buckets with the same current sum to avoid duplicate states.

        Complexity:
            Time: O(k^n) worst case with pruning significantly reducing this
            Space: O(n + k) for recursion stack and bucket array
        """

        def dfs(index: int) -> bool:
            if index == len(nums):
                return True
            for bucket in range(k):
                if bucket and buckets[bucket] == buckets[bucket - 1]:
                    continue
                buckets[bucket] += nums[index]
                if buckets[bucket] <= target and dfs(index + 1):
                    return True
                buckets[bucket] -= nums[index]
            return False

        target, remainder = divmod(sum(nums), k)
        if remainder:
            return False
        buckets = [0] * k
        nums.sort(reverse=True)
        return dfs(0)
