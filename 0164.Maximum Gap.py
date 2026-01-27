from math import inf


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """Bucket Sort Approach.

        Intuition:
            The maximum gap must be at least ceil((max - min) / (n - 1)). By
            placing elements into buckets of this size, the maximum gap must
            occur between buckets, not within them.

        Approach:
            Compute bucket size and count. Place each number into its bucket,
            tracking only min and max per bucket. The maximum gap is the largest
            difference between a bucket's minimum and the previous bucket's
            maximum.

        Complexity:
            Time: O(n) for bucket distribution and scanning
            Space: O(n) for the buckets
        """
        num_count = len(nums)
        if num_count < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        bucket_size = max(1, (max_val - min_val) // (num_count - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [[inf, -inf] for _ in range(bucket_count)]
        for val in nums:
            idx = (val - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], val)
            buckets[idx][1] = max(buckets[idx][1], val)
        result = 0
        prev_max = inf
        for bucket_min, bucket_max in buckets:
            if bucket_min > bucket_max:
                continue
            result = max(result, bucket_min - prev_max)
            prev_max = bucket_max
        return result
