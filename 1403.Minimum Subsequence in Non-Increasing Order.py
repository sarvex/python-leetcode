class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        """Find minimum subsequence with sum greater than remaining elements.

        Intuition:
            Greedily pick the largest elements until their sum exceeds
            the sum of the remaining elements.

        Approach:
            Sort in descending order. Accumulate elements until the
            accumulated sum exceeds the remainder (total - accumulated).

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for the result
        """
        result: list[int] = []
        total, accumulated = sum(nums), 0
        for value in sorted(nums, reverse=True):
            accumulated += value
            result.append(value)
            if accumulated > total - accumulated:
                break
        return result
