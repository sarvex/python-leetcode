class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """Binary search on the answer with prefix sum validation.

        Intuition:
        Binary search for the maximum average value. For each candidate average,
        check if any subarray of length >= k has average >= candidate.

        Approach:
        1. Binary search between min and max of nums.
        2. For each midpoint, subtract it from all elements and check if a subarray
           of length >= k has non-negative sum.
        3. Use prefix sums with a sliding minimum to validate efficiently.

        Complexity:
        Time: O(n * log((max - min) / epsilon))
        Space: O(1)
        """

        def check(target: float) -> bool:
            window_sum = sum(nums[:k]) - k * target
            if window_sum >= 0:
                return True
            prefix_sum = min_prefix = 0
            for i in range(k, len(nums)):
                window_sum += nums[i] - target
                prefix_sum += nums[i - k] - target
                min_prefix = min(min_prefix, prefix_sum)
                if window_sum >= min_prefix:
                    return True
            return False

        epsilon = 1e-5
        low, high = min(nums), max(nums)
        while high - low >= epsilon:
            mid = (low + high) / 2
            if check(mid):
                low = mid
            else:
                high = mid
        return low
