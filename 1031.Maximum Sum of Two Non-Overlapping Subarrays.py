from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        """Maximum Sum of Two Non-Overlapping Subarrays using prefix sums.

        Intuition:
            Use prefix sums to efficiently compute subarray sums. Try both
            orderings: first subarray before second, and second before first.

        Approach:
            Build a prefix sum array. For each ordering, slide a window and
            track the best subarray sum seen so far for the leading subarray
            while computing the trailing subarray sum at each position.

        Complexity:
            Time: O(n)
            Space: O(n) for prefix sums
        """
        length = len(nums)
        prefix = list(accumulate(nums, initial=0))
        result = best_first = 0
        i = firstLen
        while i + secondLen - 1 < length:
            best_first = max(best_first, prefix[i] - prefix[i - firstLen])
            result = max(result, best_first + prefix[i + secondLen] - prefix[i])
            i += 1
        best_second = 0
        i = secondLen
        while i + firstLen - 1 < length:
            best_second = max(best_second, prefix[i] - prefix[i - secondLen])
            result = max(result, best_second + prefix[i + firstLen] - prefix[i])
            i += 1
        return result
