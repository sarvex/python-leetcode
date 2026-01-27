class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """Prefix sum with hash map treating 0 as -1 to find equal 0s and 1s.

        Intuition:
            Replace 0s with -1s. A subarray with equal 0s and 1s now sums to 0.
            Use prefix sums to find the longest such subarray.

        Approach:
            Maintain a running sum (0 becomes -1, 1 stays 1). Store first
            occurrence of each sum. When the same sum repeats, the subarray
            between has equal 0s and 1s.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        first_occurrence = {0: -1}
        result = running_sum = 0
        for i, value in enumerate(nums):
            running_sum += 1 if value else -1
            if running_sum in first_occurrence:
                result = max(result, i - first_occurrence[running_sum])
            else:
                first_occurrence[running_sum] = i
        return result
