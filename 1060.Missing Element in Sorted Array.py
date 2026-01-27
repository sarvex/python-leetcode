class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        """Find the k-th missing number from a sorted array.

        Intuition:
            Binary search on the count of missing numbers up to each index.

        Approach:
            Define missing(i) = nums[i] - nums[0] - i. Binary search for the
            smallest index where missing(i) >= k, then compute the answer.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """

        def missing_count(index: int) -> int:
            return nums[index] - nums[0] - index

        n = len(nums)
        if k > missing_count(n - 1):
            return nums[n - 1] + k - missing_count(n - 1)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if missing_count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return nums[left - 1] + k - missing_count(left - 1)
